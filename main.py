import firebase_admin
from firebase_admin import credentials, db
import joblib # type: ignore
import pandas as pd
import numpy as np
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ----------------------------- Firebase Setup -----------------------------
# Get Firebase credentials path from environment variable
firebase_creds_path = os.getenv('FIREBASE_CREDENTIALS_PATH', 'firebase-config.json')
firebase_db_url = os.getenv('FIREBASE_DATABASE_URL')

if not os.path.exists(firebase_creds_path):
    print(f"Firebase credentials file not found: {firebase_creds_path}")
    print("Please ensure you have:")
    print("1. Created your Firebase service account JSON file")
    print("2. Set FIREBASE_CREDENTIALS_PATH in your .env file")
    exit()

if not firebase_db_url:
    print("FIREBASE_DATABASE_URL not found in environment variables")
    print("Please set FIREBASE_DATABASE_URL in your .env file")
    exit()

cred = credentials.Certificate(firebase_creds_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase_db_url
})

# Fetch indoor temperature and humidity from Firebase
ref = db.reference('/sensor_data')
sensor_data = ref.get()
user_feedback = db.reference('/user_feedback').get()

if sensor_data is None:
    print("No sensor data found in Firebase.")
    exit()

indoor_temp = sensor_data.get('indoor_temp')
indoor_humidity = sensor_data.get('indoor_humidity')
print(f"From Firebase -> Temp: {indoor_temp}°C, Humidity: {indoor_humidity}%")
activity_type = user_feedback.get('activity_type')  
status = user_feedback.get('status')  
print(f"From Firebase -> activity_type: {activity_type}°C, status: {status}%")

# ----------------------------- OpenWeather API Setup -----------------------------
API_KEY = os.getenv('OPENWEATHER_API_KEY')
LAT = os.getenv('LATITUDE', '6.9271')     # Default: Colombo
LON = os.getenv('LONGITUDE', '79.8612')

if not API_KEY:
    print("OPENWEATHER_API_KEY not found in environment variables")
    print("Please set OPENWEATHER_API_KEY in your .env file")
    exit()

weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
response = requests.get(weather_url)
weather_data = response.json()

if response.status_code != 200:
    print("Failed to get weather data from OpenWeatherMap.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    exit()

outdoor_temp = weather_data["main"]["temp"]
outdoor_humidity = weather_data["main"]["humidity"]
weather_condition = weather_data["weather"][0]["main"]
time_of_day = datetime.now().hour

print(f"From OpenWeather -> Outdoor Temp: {outdoor_temp}°C, Outdoor Humidity: {outdoor_humidity}%, Weather: {weather_condition}, Hour: {time_of_day}")

# ----------------------------- ML Prediction -----------------------------
# Load model
model = joblib.load("ac_model.pkl")
expected_features = model.feature_names_in_

# Create input dict
raw_input = {
    'indoor_temp': indoor_temp,
    'indoor_humidity': indoor_humidity,
    'occupancy': 0,  # Default or from sensor
    'time_of_day': time_of_day,
    'outdoor_temp': outdoor_temp,
    'outdoor_humidity': outdoor_humidity,
    'weather': weather_condition,
    'activity_type': activity_type,      
    'user_feedback': status    
}

# Create zeroed DataFrame with expected features
input_df = pd.DataFrame(np.zeros((1, len(expected_features))), columns=expected_features)

# Fill numeric columns
for col in ['indoor_temp', 'indoor_humidity', 'occupancy', 'time_of_day', 'outdoor_temp', 'outdoor_humidity']:
    if col in expected_features and raw_input[col] is not None:
        input_df.loc[0, col] = raw_input[col]

# Handle categorical features with one-hot
for category in ['weather', 'activity_type', 'user_feedback']:
    col_name = f"{category}_{raw_input[category]}"
    if col_name in expected_features:
        input_df.loc[0, col_name] = 1

# Predict
predicted_temp = model.predict(input_df)[0]
print(f"\n🎯 Predicted AC Set Temperature: {(predicted_temp)}°C")

# Add this after prediction
db.reference('/sensor_data/ai_set_temp').set(f"cool_{round(predicted_temp)}")
db.reference('/sensor_data/outdoor_humidity').set(outdoor_humidity)
db.reference('/sensor_data/outdoor_temp').set(outdoor_temp)
db.reference('/sensor_data/weather').set(weather_condition)
db.reference('/sensor_data/time_of_day').set(time_of_day)
db.reference('/sensor_data/timestamp').set(datetime.now().isoformat())
print(f"✅ Written to Firebase: /sensor_data/ai_set_temp -> cool_{round(predicted_temp)}")
