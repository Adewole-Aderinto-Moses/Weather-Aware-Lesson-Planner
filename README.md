# 🌦️ Automated Weather & Lesson Plan Tracker

A Python-based automation tool for educators that fetches real-time weather data to dynamically suggest lesson plans. This project was developed as part of the "Clefnet Digital Solution Tutorial" series.

## 🚀 The Problem & Solution
Educators often need to decide between indoor technical activities or outdoor logic exercises. This app removes the guesswork by using live meteorological data to provide instant pedagogical recommendations.

## 🛠️ Key Technical Features
- **Live API Integration:** Communicates with the OpenWeatherMap API to fetch real-time data for any global city.
- **Dynamic Logic Engine:** Analyzes weather descriptions (rain, clear, clouds) to trigger specific lesson plan outputs.
- **Optimized for Python 3.13:** Built using native `urllib` to bypass common library compatibility issues (like `MutableMapping` errors) in the latest Python environments.
- **Professional Terminal UI:** Uses the `Rich` library for color-coded, scannable feedback.

## 📁 Project Structure
- `weather.py`: Main logic for API connection and data parsing.
- `requirements.txt`: Project dependencies (Rich).

## 🔧 Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Adewole-Aderinto-Moses/Weather-Lesson-Planner.git](https://github.com/Adewole-Aderinto-Moses/Weather-Lesson-Planner.git)
