from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_mqtt import Mqtt
from dotenv import load_dotenv
from datetime import datetime

import os

from .weather_data import generate_test_data, generate_moon_phase_data, generate_tide_data, get_current_weather, generate_weather_week, generate_weather_hours

TIDE_CHANNEL = "weather/tide"
MOON_CHANEL = "weather/moon"
CURRENT_WEATHER_CHANNEL = "weather/current"
WEATHER_HOURS_CHANNEL = "weather/hours"
WEATHER_WEEK_CHANNEL = "weather/week"
TEST_CHANNEL = "weather/test"


TIDE_REFRESH_INTERVAL = 60 * 30 # seconds; 30 min
MOON_REFRESH_INTERVAL = 60 * 60 * 12 # seconds; 12 hr
# CURRENT_WEATHER_REFRESH_INTERVAL = 60 * 60 # seconds; 1 hr
# WEATHER_HOURS_REFRESH_INTERVAL = 60 * 60 # seconds; 1 hr
WEATHER_REFRESH_INTERVAL = 60 * 60 # seconds; 1 hr
WEATHER_WEEK_REFRESH_INTERVAL = 60 * 60 * 12 # seconds; 12 hr


load_dotenv()

app = Flask(__name__)
cors = CORS(app)
scheduler = APScheduler()
# app.config['MQTT_BROKER_URL'] = 'http://0.0.0.0:1883'
# app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = os.getenv("BACKEND_USERNAME")
app.config['MQTT_PASSWORD'] = os.getenv("BACKEND_PW")
app.config['MQTT_REFRESH_TIME'] = 10.0  # refresh time in seconds
mqtt = Mqtt(app)
scheduler.init_app(app)
scheduler.start()

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('connected')
    print(f"client {client} | userdata {userdata} | flags {flags} | rc {rc}")


# @scheduler.task('interval',id='test_job',seconds=5)
# def push_test_data():
#     mqtt.publish(TEST_CHANNEL, generate_test_data())
#     print(f'posted to test channel at {datetime.utcnow()}')

@scheduler.task('interval', id='moon', seconds=MOON_REFRESH_INTERVAL)
def push_moon_data():
    mqtt.publish(MOON_CHANEL, generate_moon_phase_data())

@scheduler.task('interval', id='tide', seconds=TIDE_REFRESH_INTERVAL)
def push_tide_data():
    mqtt.publish(TIDE_CHANNEL, generate_tide_data())

@scheduler.task('interval', id='current_weather', seconds=WEATHER_REFRESH_INTERVAL)
def push_weather_data():
    mqtt.publish(CURRENT_WEATHER_CHANNEL, get_current_weather())

@scheduler.task('interval', id='weather_week', seconds=WEATHER_WEEK_REFRESH_INTERVAL)
def push_weather_week_data():
    mqtt.publish(WEATHER_WEEK_CHANNEL, generate_weather_week())

# @scheduler.task('interval', id='weather_hours', seconds=WEATHER_HOURS_REFRESH_INTERVAL)
# def push_hourly_weather_data():
#     mqtt.publish(WEATHER_HOURS_CHANNEL, generate_weather_hours())

push_moon_data()
push_tide_data()
push_weather_data()
push_weather_week_data()

if __name__ == "__main__":
    app.run()