import streamlit as st
import requests

st.title("🌤️ Simple Weather App")

city = st.text_input("Enter city name")

if city:
    url = f"https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current_weather=true"
    response = requests.get(url)
    data = response.json()

    if "current_weather" in data:
        weather = data["current_weather"]
        st.write(f"**Temperature:** {weather['temperature']} °C")
        st.write(f"**Wind Speed:** {weather['windspeed']} km/h")
        st.write(f"**Weather Code:** {weather['weathercode']}")
    else:
        st.error("City not found or API error.")
else:
    st.info("Please enter a city name to get weather details.")
