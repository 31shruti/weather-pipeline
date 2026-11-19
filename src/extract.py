
import requests

CITIES = {
    "Jaipur": {"latitude": 26.9124, "longitude": 75.7873},
    "Delhi": {"latitude": 28.6139, "longitude": 77.2090},
    "Mumbai": {"latitude": 19.0760, "longitude": 72.8777},
    "Bengaluru": {"latitude": 12.9716, "longitude": 77.5946},
}

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(city, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation",
        "past_days": 1,
        "forecast_days": 1,
        "timezone": "Asia/Kolkata",
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()
    data["city"] = city

    return data


def extract_all():
    weather_data = []

    for city, coordinates in CITIES.items():
        print(f"Fetching weather data for {city}...")

        data = fetch_weather(
            city,
            coordinates["latitude"],
            coordinates["longitude"],
        )

        weather_data.append(data)

    return weather_data
