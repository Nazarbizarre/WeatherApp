from .. import app
from flask import request, render_template
import requests


KEY = "a1375bea9da1dde64a287e3ac2a73913"

@app.post("/weather")
def weather():
    city = request.form["city"]
    response = requests.get(f"http://127.0.0.1:8000/weather/{city}/weather")
    data = response.json()
    # weather = data["main"]
    temp = data["temp"]
    feels = data["feels_like"]
    description = "No Information" if data["description"] == 0 else data["description"]

    return render_template('result.html', city=city, temp=temp, feels=feels, description=description) 

# @app.get("/weather/<city>/<forecast_type>") # /weather/kherson/forecast|weather=weather
# def weather(city:str, forecast_type:str="weather"):
#     data = make_weather_data(city, forecast_type)
#     return jsonify(data)


# @app.route('/get_weather')
# def get_weather():
#    location = request.args.get('location')
#    if location:
#        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweather_api_key}&units=metric'
#        response = requests.get(url)
#        data = response.json()
#        return jsonify(data)
#    else:
#        return jsonify(error='Location not provided'), 400
   

# # Теперь зробимо роут для погоди на декілька днів
# @app.route('/get_weather_forecast')
# def get_weather_forecast():
#    location = request.args.get('location')
#    if location:
#        url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={openweather_api_key}&units=metric'
#        response = requests.get(url)
#        data = response.json()


#        # get weather info for nearest few days
#        forecast = []
#        print(data)
#        for entry in data['list']:
#            extracted_data = extract_weather_data(entry)
#            forecast.append(extracted_data)
#        return jsonify(forecast)
#    else:
#        return jsonify(error='Location not provided'), 400