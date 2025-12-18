import requests
from app.config import OPENWEATHER_API_KEY

def get_weather(city: str) -> str:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Sorry, I could not find weather information for {city}."

    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The temperature in {city} is {temp}°C with {description}."
