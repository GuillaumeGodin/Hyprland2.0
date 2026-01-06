#!/usr/bin/env python

import json
import requests
from datetime import datetime

# Location
CITY = "Ottawa"

WEATHER_CODES = {
    '113': '☀️ ',
    '116': '⛅ ',
    '119': '☁️ ',
    '122': '☁️ ',
    '143': '☁️ ',
    '176': '🌧️',
    '179': '🌧️',
    '182': '🌧️',
    '185': '🌧️',
    '200': '⛈️ ',
    '227': '🌨️',
    '230': '🌨️',
    '248': '☁️ ',
    '260': '☁️ ',
    '263': '🌧️',
    '266': '🌧️',
    '281': '🌧️',
    '284': '🌧️',
    '293': '🌧️',
    '296': '🌧️',
    '299': '🌧️',
    '302': '🌧️',
    '305': '🌧️',
    '308': '🌧️',
    '311': '🌧️',
    '314': '🌧️',
    '317': '🌧️',
    '320': '🌨️',
    '323': '🌨️',
    '326': '🌨️',
    '329': '❄️ ',
    '332': '❄️ ',
    '335': '❄️ ',
    '338': '❄️ ',
    '350': '🌧️',
    '353': '🌧️',
    '356': '🌧️',
    '359': '🌧️',
    '362': '🌧️',
    '365': '🌧️',
    '368': '🌧️',
    '371': '❄️',
    '374': '🌨️',
    '377': '🌨️',
    '386': '🌨️',
    '389': '🌨️',
    '392': '🌧️',
    '395': '❄️ '
}

data = {}

# Fetch weather with f-string for City and Error Handling
try:
    weather = requests.get(f"https://wttr.in/{CITY}?format=j1").json()
except Exception as e:
    print(json.dumps({"text": "Err", "tooltip": str(e)}))
    exit()

def format_time(time):
    return time.replace("00", "").zfill(2)

def format_temp(temp):
    # Using the passed temp variable directly
    return (temp + "°").ljust(3)

def format_chances(hour):
    chances = {
        "chanceoffog": "Fog",
        "chanceoffrost": "Frost",
        "chanceofovercast": "Overcast",
        "chanceofrain": "Rain",
        "chanceofsnow": "Snow",
        "chanceofsunshine": "Sunshine",
        "chanceofthunder": "Thunder",
        "chanceofwindy": "Wind"
    }

    conditions = []
    for event in chances.keys():
        if int(hour[event]) > 0:
            conditions.append(chances[event]+" "+hour[event]+"%")
    return ", ".join(conditions)

# Current conditions logic
curr_cond = weather['current_condition'][0]
tempint = int(curr_cond['FeelsLikeF'])
extrachar = ''
if 0 < tempint < 10:
    extrachar = '+'

# Output for Waybar (Preserving your exact original formatting)
data['text'] = ' ' + WEATHER_CODES[curr_cond['weatherCode']] + \
    " " + extrachar + curr_cond['FeelsLikeF'] + "°"

data['tooltip'] = f"<b>{CITY}: {curr_cond['weatherDesc'][0]['value']} {curr_cond['temp_F']}°</b>\n"
data['tooltip'] += f"Feels like: {curr_cond['FeelsLikeF']}°\n"
data['tooltip'] += f"Wind: {curr_cond['windspeedKmph']}Km/h\n"
data['tooltip'] += f"Humidity: {curr_cond['humidity']}%\n"

for i, day in enumerate(weather['weather']):
    data['tooltip'] += f"\n<b>"
    if i == 0:
        data['tooltip'] += "Today, "
    if i ==