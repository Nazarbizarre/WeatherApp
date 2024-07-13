from .. import app
from os import getenv
from ..utils import WeatherApp
from dotenv import load_dotenv

load_dotenv()


weather_app = WeatherApp(getenv("API_KEY"))


@app.get("/weather/{city}")
@app.get("/weather/{city}/{forecast_type}")
def weather(city:str, forecast_type:str="weather"):
    # print(weather_app.extract("dnipro", "weather"))
    weather = weather_app.extract(city, forecast_type)
    args = ("temp", "feels_like") 
    data = weather_app.transform(weather, "main", *args)
    description = weather_app.transform(weather, "weather", "description")
    data.update(description)
    print(data) 
    return data