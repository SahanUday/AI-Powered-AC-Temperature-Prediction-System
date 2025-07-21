# 🌬️ AI-Powered AC Temperature Prediction System

**AI-Powered AC Temperature Prediction System** is an intelligent air conditioner temperature predicting system that optimizes indoor temperature settings using machine learning, real-time sensor data, and external weather conditions. Developed in Python, it integrates with Firebase for data storage and retrieval, and uses the OpenWeather API to fetch outdoor weather conditions. The system predicts optimal AC set temperatures based on indoor conditions, user feedback, and environmental factors.

---

## 📌 Overview

The **AI-Powered AC Temperature Prediction System** is designed to enhance comfort and energy efficiency by dynamically adjusting air conditioner settings. It:

- Collects **indoor temperature and humidity** from sensors stored in Firebase.
- Fetches **outdoor weather data** (temperature, humidity, weather condition) via the OpenWeather API.
- Uses a pre-trained **machine learning model** to predict the optimal AC temperature.
- Incorporates **user feedback** and **activity type** to personalize predictions.
- Updates Firebase with predicted temperatures and environmental data for real-time control.

This project is ideal for smart home applications, energy-efficient HVAC systems, or IoT-based climate control solutions.

---

## 🔍 Key Features

- 🌡️ **Real-Time Sensor Data**: Retrieves indoor temperature and humidity from Firebase.
- ☁️ **Weather Integration**: Fetches outdoor weather data using the OpenWeather API.
- 🧠 **ML Predictions**: Uses a pre-trained model to predict optimal AC set temperatures.
- 🕹️ **User Feedback**: Incorporates user activity and comfort feedback for personalized settings.
- 📡 **Firebase Integration**: Stores and retrieves data for seamless real-time operation.
- 🔄 **Continuous Operation**: Runs in a loop, updating predictions every 20 seconds.
- ⚡ **Energy Efficiency**: Optimizes AC settings to balance comfort and energy usage.

---

## 🔧 Technologies & Tools Used

- **Python 3.10+** – Core programming language
- **Firebase Admin SDK** – For real-time database integration
- **Joblib** – For loading the pre-trained ML model
- **Pandas & NumPy** – For data manipulation and preparation
- **Requests** – For OpenWeather API calls
- **OpenWeather API** – For fetching outdoor weather data
- **Python-dotenv** – For environment variable management

> ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=FFFF00)
> ![Firebase](https://img.shields.io/badge/firebase-%23FFCA28.svg?logo=firebase&logoColor=black)
> ![OpenWeather](https://img.shields.io/badge/OpenWeather-%2300AEEF?logo=weather&logoColor=white)

---

## 📊 Dataset

The machine learning model was trained on a dataset with the following features:

| Feature             | Description                              |
|--------------------|------------------------------------------|
| `indoor_temp`      | Indoor temperature (°C)                  |
| `indoor_humidity`  | Indoor humidity (%)                      |
| `occupancy`        | Room occupancy (0 or 1)                  |
| `weather`          | Outdoor weather condition (e.g., Clear, Rain) |
| `time_of_day`      | Hour of the day (0–23)                   |
| `outdoor_temp`     | Outdoor temperature (°C)                  |
| `outdoor_humidity` | Outdoor humidity (%)                      |
| `user_feedback`    | User comfort feedback (e.g., Comfortable, Too cold) |
| `activity_type`    | User activity (e.g., Relaxing)            |
| `last_set_temp`    | Previous AC set temperature (°C)          |

A small sample of the dataset is included in the project description for reference.

---

## ⚙️ How It Works

1. **Sensor Data Retrieval**: Fetches indoor temperature, humidity, user feedback, and activity type from Firebase.
2. **Weather Data Fetching**: Queries the OpenWeather API for outdoor temperature, humidity, and weather conditions.
3. **Data Preparation**: Combines sensor and weather data into a format compatible with the ML model.
4. **Prediction**: Uses the pre-trained model to predict the optimal AC set temperature.
5. **Firebase Update**: Writes the predicted temperature and environmental data back to Firebase.
6. **Continuous Loop**: Repeats every 20 seconds to ensure real-time adjustments.

---

## 🧰 Setup & Run Guide

### ✅ Requirements

- Python 3.10+
- All dependencies listed in `requirements.txt`
- Firebase Admin SDK credentials
- OpenWeather API key
- Pre-trained ML model (`ac_model.pkl`)

### 🔐 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SahanUday/AI-Powered-AC-Temperature-Prediction-System.git
   cd AI-Powered-AC-Temperature-Prediction-System
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Copy the environment template:
     ```bash
     cp .env.template .env
     ```
   - Edit `.env` file and add your actual values:
     ```
     OPENWEATHER_API_KEY=your_openweather_api_key_here
     LATITUDE=your_latitude
     LONGITUDE=your_longitude
     FIREBASE_CREDENTIALS_PATH=your_firebase_credentials.json
     FIREBASE_DATABASE_URL=https://your-project-default-rtdb.region.firebasedatabase.app/
     ```

4. **Set Up Firebase Credentials**:
   - Download your Firebase Admin SDK service account JSON file from Firebase Console
   - Save it in your project directory (the filename should match `FIREBASE_CREDENTIALS_PATH` in your `.env`)
   - **Important**: This file contains sensitive data and should NEVER be committed to version control

5. **Get OpenWeather API Key**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get your free API key
   - Add it to your `.env` file

6. **Place the ML Model**:
   - Ensure the pre-trained model file (`ac_model.pkl`) is in the project root.

7. **Run the Project**:
   ```bash
   python main.py
   ```

   The script will fetch data from Firebase and OpenWeather API, make predictions, and update Firebase with the results.

---

## 📜 Project Structure

```
AI-Powered-AC-Temperature-Prediction-System/
├── main.py               # Main script with ML prediction logic
├── ac_model.pkl                  # Pre-trained ML model
├── requirements.txt              # Python dependencies
├── .env.template                 # Environment variables template
├── firebase-config-template.json # Firebase credentials template
├── .gitignore                    # Git ignore rules (protects sensitive files)
├── README.md                     # Project documentation
└── .env                          # Your environment variables 
```

### 🔒 **Important Files (Not in Repository)**:
- `.env` - Your actual environment variables with API keys
- `your_firebase_credentials.json` - Your Firebase service account file

These files are automatically excluded by `.gitignore` to protect your sensitive data.

## 🔐 Security Features

This project implements several security best practices:

- **Environment Variables**: All sensitive data (API keys, database URLs) stored in `.env` file
- **Template Files**: Safe templates provided for configuration without exposing real credentials
- **Git Ignore**: Comprehensive `.gitignore` prevents accidental commit of sensitive files
- **No Hardcoded Secrets**: No API keys or credentials hardcoded in source code
- **Service Account**: Uses Firebase service account for secure database access

## 🚀 Usage

1. **First Run**: The script will validate your environment configuration
2. **Data Fetching**: Retrieves indoor sensor data from Firebase
3. **Weather Data**: Fetches outdoor conditions from OpenWeather API
4. **ML Prediction**: Uses the trained model to predict optimal AC temperature
5. **Firebase Update**: Writes prediction and environmental data back to Firebase

## 📊 Sample Output

```
From Firebase -> Temp: 26.5°C, Humidity: 65%
From Firebase -> activity_type: Relaxing, status: Comfortable
From OpenWeather -> Outdoor Temp: 28.3°C, Outdoor Humidity: 78%, Weather: Clear, Hour: 14

🎯 Predicted AC Set Temperature: 24.2°C

✅ Written to Firebase: /sensor_data/ai_set_temp -> cool_24
```

---

## 🤝 Contribution

Contributions are welcome! Potential enhancements include:
- 📈 Adding support for multiple rooms or zones
- 🧠 Improving the ML model with more features
- 🖥️ Building a web dashboard for monitoring
- 🔌 Integrating with IoT devices for direct AC control
- 🔒 Adding authentication and user management
- 📱 Creating a mobile app interface

### Contributing Guidelines:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. **Never commit sensitive files** (`.env`, credentials)
4. Test your changes thoroughly
5. Commit your changes (`git commit -m "Add your feature"`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Submit a pull request
