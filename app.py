from flask import Flask, render_template, request, redirect, url_for
import requests
from DataBase import save_weather_query,get_weather_history,create_table
from utils import timestamp_to_hms_format, wind_direction, hpa_to_mmhg
import os
import json
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__, static_folder="www/files", template_folder="www")
create_table()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        city_name=request.form['city']
        weather_data=get_weather_data(city_name)
        if weather_data:
            save_weather_query(weather_data["name"],
                               weather_data["weather"][0]['main'],
                               weather_data["weather"][0]["description"],
                               weather_data["main"]["temp"],
                               weather_data["main"]["feels_like"],
                               weather_data["main"]["humidity"],
                               hpa_to_mmhg(weather_data["main"]["pressure"]),
                               weather_data["wind"]["speed"],
                               wind_direction(weather_data["wind"]["deg"]),
                               timestamp_to_hms_format(weather_data["sys"]["sunrise"], weather_data["timezone"]),
                               timestamp_to_hms_format(weather_data["sys"]["sunset"], weather_data["timezone"]),
                               timestamp_to_hms_format(weather_data["dt"],weather_data["timezone"]),
                               json.dumps(weather_data))
            return render_template('index.html',
                                   weather=[weather_data["name"],
                                            weather_data["weather"][0]["main"],
                                            weather_data["weather"][0]["description"],
                                            weather_data["main"]["temp"],
                                            weather_data["main"]["feels_like"],
                                            weather_data["main"]["humidity"],
                                            hpa_to_mmhg(weather_data["main"]["pressure"]),
                                            weather_data["wind"]["speed"],
                                            wind_direction(weather_data["wind"]["deg"]),
                                            timestamp_to_hms_format(weather_data["sys"]["sunrise"], weather_data["timezone"]),
                                            timestamp_to_hms_format(weather_data["sys"]["sunset"], weather_data["timezone"]),
                                            timestamp_to_hms_format(weather_data["dt"],weather_data["timezone"])],
                                   icon=weather_data["weather"][0]['icon'],
                                   isWeather=True)
        else:
            return render_template('index.html', isWeather=False)
    return render_template('index.html', isWeather=False)

@app.route('/history')
def history():
    history=get_weather_history()
    return render_template('history.html',history=history)

def get_weather_data(city_name):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.getenv('WEATHER_API_KEY')}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=os.getenv('APP_HOST_PORT'),debug=True)