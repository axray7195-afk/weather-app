import streamlit as st
import requests

# ---------- Page Setup ----------
st.set_page_config(page_title="Aesthetic Weather App", page_icon="🌤️", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            font-family: 'Poppins', sans-serif;
        }

        /* Center content */
        .block-container {
            padding-top: 3rem;
            text-align: center;
        }

        h1 {
            color: #ffffff;
            font-weight: 700;
            font-size: 2.5rem;
        }

        p {
            color: #e0e0e0;
            font-size: 1rem;
        }

        /* Input box */
        input {
            background-color: rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 10px !important;
        }

        /* Result card */
        .weather-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.2);
            margin-top: 30px;
            transition: 0.3s ease;
        }

        .weather-card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 35px rgba(255, 255, 255, 0.3);
        }

        .emoji {
            font-size: 50px;
            animation: float 2s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .main-temp {
            color: #FFD700;
            font-size: 3rem;
            margin: 10px 0;
        }

        .info {
            color: #B0C4DE;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- App Title ----------
st.markdown("""
    <h1>🌤️ Aesthetic Weather App</h1>
    <p>Get real-time weather updates with style ✨</p>
""", unsafe_allow_html=True)

# ---------- Input ----------
city = st.text_input("🏙️ Enter city name")

if city:
    api_key = "3a9e0e4693504cbbb0585105250811"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"].capitalize()

        # Emoji / Icon Mapping
        weather_icons = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Haze": "🌁"
        }
        icon = weather_icons.get(condition, "🌎")

        # ---------- Display ----------
        st.markdown(f"""
            <div class="weather-card">
                <div class="emoji">{icon}</div>
                <h2>{city.title()}</h2>
                <p style="font-size:1.1rem;">{description}</p>
                <div class="main-temp">{temp}°C</div>
                <p class="info">💧 Humidity: {humidity}% &nbsp; | &nbsp; 🌬️ Wind: {wind_speed} m/s</p>
                <p class="info">📊 Pressure: {pressure} hPa</p>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.error("❌ City not found. Please try again.")
else:
    st.info("ℹ️ Please enter a city name to get weather details.")
