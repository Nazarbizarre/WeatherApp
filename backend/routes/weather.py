from .. import app
from os import getenv
from ..utils import WeatherApp
from dotenv import load_dotenv

load_dotenv()


weather_app = WeatherApp("a1375bea9da1dde64a287e3ac2a73913")


@app.get("/weather/{city}/{forecast_type}")
def weather(city:str, forecast_type:str):
    data = weather_app.make_response(city, forecast_type)
    return (data)