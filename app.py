import streamlit as st
import requests

# ---------- Page setup ----------
st.set_page_config(page_title="Aesthetic Weather App", page_icon="🌤️", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        .stApp {
            background: linear-gradient(135deg, #1E3C72 0%, #2A5298 100%);
            color: white;
            font-family: 'Poppins', sans-serif;
        }

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
            color: #d0d0d0;
            font-size: 1rem;
        }

        /* Input field */
        input {
            background-color: rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }

        /* Weather Card */
        .weather-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
            margin-top: 30px;
            transition: all 0.3s ease;
        }

        .weather-card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 40px rgba(255, 255, 255, 0.3);
        }

        .emoji {
            font-size: 60px;
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

# ---------- Title ----------
st.markdown("""
    <h1>🌤️ Aesthetic Weather App</h1>
    <p>Real-time weather updates with a beautiful touch ✨</p>
""", unsafe_allow_html=True)

# ---------- Input ----------
city = st.text_input("🏙️ Enter city name")

if city:
    api_key = "3a9e0e4693504cbbb0585105250811"  # Replace with your actual API key
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=10)
        data = response.json()

        # Handle invalid location
        if response.status_code != 200 or data.get("cod") != 200:
            st.warning("⚠️ Location not found. Please try a valid city name.")
        else:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            condition = data["weather"][0]["main"]
            description = data["weather"][0]["description"].capitalize()

            # Emoji Mapping
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
            icon = weather_icons.get(condition, "🌍")

            # Display Weather Info
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

    except requests.exceptions.RequestException:
        st.error("⚠️ Network error. Please check your connection and try again.")
else:
    st.info("ℹ️ Please enter a city name to get weather details.")
