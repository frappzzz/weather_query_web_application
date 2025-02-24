from flask import Flask, render_template, request, redirect, url_for
import requests
from DataBase import save_weather_query,get_weather_history
from utils import timestamp_to_hms_format, wind_direction
import config
app = Flask(__name__, static_folder=config.APP_STATIC_FOLDER, template_folder=config.APP_TEMPLATE_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="GET":
        weather_data=get_weather_data("Minsk")
        print(weather_data["weather"][0]['main'], weather_data["weather"][0]['description'], weather_data["main"]['temp'],weather_data["main"]['feels_like'], weather_data["wind"]["speed"],wind_direction(weather_data["wind"]["deg"]),timestamp_to_hms_format(weather_data["sys"]["sunrise"]),timestamp_to_hms_format(weather_data["sys"]["sunset"]))
        return weather_data
@app.route('/history')
def history():
    history=get_weather_history()
    return render_template('history.html',history=history)


def get_weather_data(city_name):
    url=f"{config.WEATHER_API_URL}?q={city_name}&appid={config.WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)