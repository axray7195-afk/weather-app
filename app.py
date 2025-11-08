import streamlit as st
import requests

# App config
st.set_page_config(page_title="Weather App", page_icon="🌦️", layout="centered")

# ---- CSS STYLING ----
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1280&q=80');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {background: rgba(0,0,0,0);}
[data-testid="stToolbar"] {right: 2rem;}
h1, h2, h3, h4, h5, h6, p, span {
    color: #ffffff !important;
    text-align: center;
}
.css-1d391kg {background-color: rgba(0,0,0,0.5) !important; border-radius: 20px !important;}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- TITLE ----
st.markdown("<h1 style='text-align:center;'>🌦️ Simple Weather App</h1>", unsafe_allow_html=True)

# ---- Helper functions ----
def get_lat_lon(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_response = requests.get(geo_url)
    if geo_response.status_code == 200:
        geo_data = geo_response.json()
        if "results" in geo_data and len(geo_data["results"]) > 0:
            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]
            return lat, lon
    return None, None


def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


# ---- Weather icon mapping ----
def get_weather_icon(code):
    icons = {
        0: "☀️ Clear sky",
        1: "🌤️ Mainly clear",
        2: "⛅ Partly cloudy",
        3: "☁️ Overcast",
        45: "🌫️ Fog",
        48: "🌫️ Depositing rime fog",
        51: "🌦️ Light drizzle",
        53: "🌧️ Moderate drizzle",
        55: "🌧️ Heavy drizzle",
        61: "🌦️ Light rain",
        63: "🌧️ Moderate rain",
        65: "🌧️ Heavy rain",
        71: "❄️ Snow fall",
        73: "❄️ Moderate snow",
        75: "❄️ Heavy snow",
        95: "⛈️ Thunderstorm",
        99: "🌩️ Thunderstorm with hail",
    }
    return icons.get(code, "🌈 Weather data")

# ---- Input ----
city = st.text_input("Enter city name", placeholder="e.g., Berlin, Mumbai, Paris")

# ---- Main logic ----
if st.button("Get Weather"):
    if city:
        lat, lon = get_lat_lon(city)
        if lat and lon:
            data = get_weather(lat, lon)
            if data and "current_weather" in data:
                weather = data["current_weather"]
                code = weather.get("weathercode", 0)
                icon = get_weather_icon(code)
                
                st.markdown(
                    f"""
                    <div style="background-color:rgba(0,0,0,0.6);
                                padding:20px; border-radius:20px; text-align:center;">
                        <h2>{icon}</h2>
                        <h3>🌆 {city.title()}</h3>
                        <p>🌡️ Temperature: {weather['temperature']}°C</p>
                        <p>🌬️ Wind Speed: {weather['windspeed']} km/h</p>
                        <p>⏰ Time: {weather['time']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.error("❌ Could not fetch weather data.")
        else:
            st.error("❌ City not found.")
    else:
        st.warning("Please enter a city name.")
