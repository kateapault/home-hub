import datetime
import ephem
import requests
import json

from helpers import convert_to_celcius
from dummy_data import static_weather_data
from mapping import weather_descriptions, weather_emojis, map_degree_to_direction, map_moon_icon_and_phase


LATITUDE = 38.814550
LONGITUDE = -77.051940

# r_weather = requests.get('https://api.open-meteo.com/v1/forecast?latitude=38.81455&longitude=-77.05194&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,weathercode,windspeed_10m,winddirection_10m,windgusts_10m&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,weathercode&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York')
# weather_json = r_weather.json()

def generate_test_data():
    return '{"text": "hi test yes :)"}'

def generate_moon_phase_data():
    moon_phase_data = {}
    observer = ephem.Observer()
    observer.lat = LATITUDE
    observer.long = LONGITUDE

    today_str = datetime.datetime.now().strftime('%Y/%m/%d')
    observer.date = today_str
    moon = ephem.Moon()
    moon.compute(observer)

    next_full_moon = str(ephem.next_full_moon(today_str)).split(' ')[0]
    next_new_moon = str(ephem.next_new_moon(today_str)).split(' ')[0]

    moon_phase_data["next_full_moon"] = next_full_moon
    moon_phase_data["next_new_moon"] = next_new_moon

    waxing = ephem.next_full_moon(today_str) < ephem.next_new_moon(today_str)
    moon_lit = moon.moon_phase * 100
    moon_data = map_moon_icon_and_phase(moon_lit, waxing)
    moon_phase_data["moon_phase"] = moon_data["moon_phase"]
    moon_phase_data["moon_icon"] = moon_data["moon_icon"]

    return json.dumps(moon_phase_data)

def generate_tide_data():
    begin_date = datetime.date.today().strftime('%Y%m%d')
    end_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y%m%d')
    station = "8594900"
    r_tide_data = requests.get(f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date={begin_date}&end_date={end_date}&station={station}&product=predictions&datum=MLLW&time_zone=lst_ldt&interval=hilo&units=english&application=DataAPI_Sample&format=json")
    tide_points = r_tide_data.json()['predictions']
    # print(tide_points)
    # dummy data to prevent jillion calls:
    # tide_points = [{'t': '2024-07-11 00:33', 'v': '2.907', 'type': 'H'}, {'t': '2024-07-11 07:12', 'v': '0.732', 'type': 'L'}, {'t': '2024-07-11 12:39', 'v': '2.890', 'type': 'H'}, {'t': '2024-07-11 19:32', 'v': '0.581', 'type': 'L'}, {'t': '2024-07-12 01:15', 'v': '2.917', 'type': 'H'}, {'t': '2024-07-12 07:55', 'v': '0.782', 'type': 'L'}, {'t': '2024-07-12 13:25', 'v': '2.787', 'type': 'H'}, {'t': '2024-07-12 20:03', 'v': '0.614', 'type': 'L'}]
    # tide_points = [{'t': '2024-02-21 00:33', 'v': '-0.150', 'type': 'L'}, {'t': '2024-02-21 05:54', 'v': '2.154', 'type': 'H'}, {'t': '2024-02-21 12:34', 'v': '-0.043', 'type': 'L'}, {'t': '2024-02-21 18:08', 'v': '2.342', 'type': 'H'}, {'t': '2024-02-22 01:22', 'v': '-0.196', 'type': 'L'}, {'t': '2024-02-22 06:43', 'v': '2.253', 'type': 'H'}, {'t': '2024-02-22 13:26', 'v': '-0.107', 'type': 'L'}, {'t': '2024-02-22 18:57', 'v': '2.376', 'type': 'H'}]
    points_found = False
    i = 0
    while not points_found:
        tide_time = datetime.datetime.strptime(tide_points[i]['t'],'%Y-%m-%d %H:%M')
        if tide_time > datetime.datetime.now():
            if tide_points[i]['type'] == 'H':
                next_high_tide = tide_points[i]['t']
                next_low_tide = tide_points[i+1]['t']
                tide_status = "Rising"
            else:
                next_low_tide = tide_points[i]['t']
                next_high_tide = tide_points[i+1]['t']
                tide_status = "Ebbing"
            points_found = True
        i += 1
    next_point = datetime.datetime.strptime(next_high_tide,'%Y-%m-%d %H:%M') if tide_status == "Rising" else datetime.datetime.strptime(next_low_tide,'%Y-%m-%d %H:%M')
    if next_point - datetime.datetime.now() > datetime.timedelta(hours=4):
        emojis = "🌊" if tide_status == 'Rising' else "🌊🌊🌊"
    elif next_point - datetime.datetime.now() > datetime.timedelta(hours=2):
        emojis = "🌊🌊"
    else:
        emojis = "🌊🌊🌊" if tide_status == 'Rising' else "🌊"
    tide_data = {
        "next_low_tide": next_low_tide,
        "next_high_tide": next_high_tide,
        "tide_status": tide_status,
        "emojis": emojis
    }
    return json.dumps(tide_data)

def get_current_weather():
    r_weather = requests.get('https://api.open-meteo.com/v1/forecast?latitude=38.81455&longitude=-77.05194&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,weathercode,windspeed_10m,winddirection_10m,windgusts_10m&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,weathercode&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York')
    weather_json = r_weather.json()
    # print(weather_json)
    # to avoid a jillion calls:
    # weather_json = static_weather_data
    current_weather = {
        "temperature_f": weather_json["current"]["temperature_2m"],
        "temperature_c": convert_to_celcius(weather_json["current"]["temperature_2m"]),
        "relative_humidity": weather_json["current"]["relativehumidity_2m"],
        "apparent_temp_f": weather_json["current"]["apparent_temperature"],
        "apparent_temp_c": convert_to_celcius(weather_json["current"]["apparent_temperature"]),
        "weather_description": weather_descriptions[weather_json["current"]["weathercode"]],
        "weather_emoji": weather_emojis[weather_json["current"]["weathercode"]],
        "precipitation": weather_json["current"]["precipitation"],
        "wind_speed": weather_json["current"]["windspeed_10m"],
        "wind_direction": map_degree_to_direction(weather_json["current"]["winddirection_10m"]),
        "wind_gusts": weather_json["current"]["windgusts_10m"]
    }
    return json.dumps(current_weather)


def generate_weather_week():
    r_weather = requests.get('https://api.open-meteo.com/v1/forecast?latitude=38.81455&longitude=-77.05194&current=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,weathercode,windspeed_10m,winddirection_10m,windgusts_10m&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,apparent_temperature,precipitation_probability,precipitation,weathercode&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,precipitation_probability_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York')
    weather_json = r_weather.json()
    # weather_json = static_weather_data['daily']

    weather_week = []
    for i in range(len(weather_json['time'])):
        weather_week += [{
            "date": weather_json['time'][i],
            "precipitation_chance": weather_json['precipitation_probability_max'][i],
            "sunrise": weather_json['sunrise'][i],
            "sunset": weather_json['sunset'][i],
            "weather_description": weather_descriptions[weather_json['weathercode'][i]],
            "weather_emoji": weather_emojis[weather_json['weathercode'][i]],
            "maxTempF": weather_json['temperature_2m_max'][i],
            "maxTempC": convert_to_celcius(weather_json['temperature_2m_max'][i]),
            "minTempF": weather_json['temperature_2m_min'][i],
            "minTempC": convert_to_celcius(weather_json['temperature_2m_min'][i]),
        }]
    return json.dumps(weather_week)