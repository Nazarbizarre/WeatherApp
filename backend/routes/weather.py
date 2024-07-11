from .. import app
from os import getenv
from ..utils import WeatherApp
from dotenv import load_dotenv

load_dotenv()


weather_app = WeatherApp(getenv("API_KEY"))


@app.get("/weather/{city}")
@app.get("/weather/{city}/{forecast_type}")
def weather(city:str, forecast_type:str="weather"):
    weather = weather_app.extract(city, forecast_type) 
    # data = weather_app.transform(weather, "temp", "feels_like", json=weather)
    data = {
        "temp": weather_app.transform(weather, "main", "temp"),
        "feels_like": weather_app.transform(weather, "main", "feels_like"),
        "description": weather_app.transform(weather, "weather", "description")
    }
    return data