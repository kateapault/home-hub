from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_mqtt import Mqtt
from dotenv import load_dotenv
from datetime import datetime

import os

from weather_data import generate_test_data, generate_moon_phase_data

TIDE_CHANNEL = "weather/tide"
MOON_CHANEL = "weather/moon"
CURRENT_WEATHER_CHANNEL = "weather/current"
HOURLY_WEATHER_CHANNEL = "weather/hourly"
WEEKLY_WEATHER_CHANNEL = "weather/week"
TEST_CHANNEL = "weather/test"

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


@app.route("/test")
def test_mqtt():
    mqtt.publish(TEST_CHANNEL,'{"text": "hi this is from the /test route"}')
    return "<h1>hi yes sent 'HI TESTING' :)</h1>"

@app.route("/test/moon")
def send_moon():
    moon_data = generate_moon_phase_data()
    mqtt.publish(MOON_CHANEL, str(moon_data))
    return "hi yes sent moon phase"

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('connected')
    print(f"client {client} | userdata {userdata} | flags {flags} | rc {rc}")


@scheduler.task('interval',id='test_job',seconds=5)
def push_test_data():
    mqtt.publish(TEST_CHANNEL, generate_test_data())
    print(f'posted to test channel at {datetime.utcnow()}')


def push_moon_data():
    mqtt.publish(MOON_CHANEL, generate_moon_phase_data())


def push_tide_data():
    pass


def push_current_weather_data():
    pass


def push_hourly_weather_data():
    pass

def push_daily_weather_data():
    pass




if __name__ == "__main__":
    app.run()