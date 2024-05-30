from flask import Flask
from flask_cors import CORS
from flask_mqtt import Mqtt
from dotenv import load_dotenv

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
app.config['MQTT_USERNAME'] = os.getenv("BACKEND_USERNAME")
app.config['MQTT_PASSWORD'] = os.getenv("BACKEND_PW")
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"


@app.route("/test")
def test_mqtt():
    mqtt.publish(TEST_CHANNEL,'{"text": "hi this is from the /test route"}')
    return "hi yes sent 'HI TESTING' :)"

@app.route("/test/moon")
def send_moon():
    moon_data = generate_moon_phase_data()
    mqtt.publish(MOON_CHANEL, str(moon_data))
    return "hi yes sent moon phase"

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print('connected')
    print(f"client {client} | userdata {userdata} | flags {flags} | rc {rc}")


def push_test_data():
    mqtt.publish(TEST_CHANNEL, generate_test_data())


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