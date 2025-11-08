import streamlit as st
import requests

# ---------- Page setup ----------
st.set_page_config(page_title="Simple Weather App", page_icon="🌤️", layout="centered")

# ---------- Title ----------
st.markdown(
    """
    <h1 style="text-align:center; color:#ffffff;">🌤️ Simple Weather App</h1>
    <p style="text-align:center; color:#a0a0a0;">Get real-time weather updates anywhere in the world</p>
    """,
    unsafe_allow_html=True,
)

# ---------- Input ----------
city = st.text_input("🌍 Enter city name")

if city:
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
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

        # Emoji for condition
        weather_icons = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Drizzle": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
        }
        icon = weather_icons.get(condition, "🌍")

        # Display results in a nice container
        st.markdown(
            f"""
            <div style="background-color:#1E1E2F;padding:20px;border-radius:15px;text-align:center;">
                <h2 style="color:#ffffff;">{icon} {city.title()}</h2>
                <p style="color:#00BFFF;font-size:22px;margin:0;">{description}</p>
                <h1 style="color:#FFD700;margin:10px 0;">{temp}°C</h1>
                <p style="color:#cccccc;">💧 Humidity: {humidity}% &nbsp;&nbsp;🌬️ Wind: {wind_speed} m/s</p>
                <p style="color:#cccccc;">📊 Pressure: {pressure} hPa</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        st.error("❌ City not found. Please try again.")
else:
    st.info("ℹ️ Please enter a city name to get weather details.")
