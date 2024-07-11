from requests import get


class WeatherApp:
    base_url: str = "http://api.openweathermap.org/data/2.5/"

    def __init__(self, api_key:str):
        self.api_key = api_key

    def __get_params(self, city, units:str = "metric"):
        return {
            "q": city,
            "appid": self.api_key,
            "units": units,
        }

    def make_response(self, city, forecast_type):
        response = get(
            url=f"{self.base_url}{forecast_type}",
            params=self.__get_params(city)
        )
        return response.json()