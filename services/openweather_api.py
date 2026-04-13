import requests
from common.tools import convert_to_celsius, convert_to_kmh

from datetime import datetime
from config import Config

def get_weather():

    API_KEY = Config.API_KEY # Nie powinnien byc widoczny
    city = Config.API_CITY

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        record = {
            "city": data.get("name"),

            "temp": convert_to_celsius(data.get("main").get("temp")),
            "feels_like": convert_to_celsius(data.get("main").get("feels_like")),

            "wind": convert_to_kmh(data.get("wind").get("speed")),

            "humidity": data.get("main").get("humidity"),
            "pressure": data.get("main").get("pressure"),

            "description": data.get("weather")[0].get("description"),

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return record
    except Exception as e:
        print(e)
