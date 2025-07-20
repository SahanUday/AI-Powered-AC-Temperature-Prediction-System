# 🌬️ AI-Powered AC Temperature Prediction System

**AI-Powered AC Temperature Prediction System** is an intelligent air conditioning control system that optimizes indoor temperature settings using machine learning, real-time sensor data, and external weather conditions. Developed in Python, it integrates with Firebase for data storage and retrieval, and uses the OpenWeather API to fetch outdoor weather conditions. The system predicts optimal AC set temperatures based on indoor conditions, user feedback, and environmental factors.

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
- Firebase Admin SDK: `pip install firebase-admin`
- Joblib: `pip install joblib`
- Pandas: `pip install pandas`
- NumPy: `pip install numpy`
- Requests: `pip install requests`
- Pre-trained ML model (`ac_model.pkl`)
- Firebase credentials JSON file (`airvix-ef027-firebase-adminsdk-fbsvc-18f86681a5.json`)
- OpenWeather API key

### 🔐 Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SahanUday/SmartClimateAI.git
   cd SmartClimateAI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Firebase**:
   - Place your Firebase credentials JSON file (`airvix-ef027-firebase-adminsdk-fbsvc-18f86681a5.json`) in the project root.
   - Ensure the Firebase Realtime Database URL is correctly configured in the code.

4. **Set Up OpenWeather API Key**:
   - Replace the `API_KEY` in the code with your OpenWeather API key:
     ```python
     API_KEY = "your_openweather_api_key_here"
     ```

5. **Place the ML Model**:
   - Ensure the pre-trained model file (`ac_model.pkl`) is in the project root.

6. **Run the Project**:
   ```bash
   python main.py
   ```

   The script will run continuously, fetching data, making predictions, and updating Firebase every 20 seconds.

---

## 📜 Project Structure

```
SmartClimateAI/
├── main.py                    # Main script with ML prediction logic
├── ac_model.pkl              # Pre-trained ML model
├── airvix-ef027-firebase-adminsdk-fbsvc-18f86681a5.json  # Firebase credentials
├── requirements.txt           # Python dependencies
├── README.md                 # Project documentation
```

---

## 🤝 Contribution

Contributions are welcome! Potential enhancements include:
- 📈 Adding support for multiple rooms or zones
- 🧠 Improving the ML model with more features
- 🖥️ Building a web dashboard for monitoring
- 🔌 Integrating with IoT devices for direct AC control

To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Submit a pull request.
