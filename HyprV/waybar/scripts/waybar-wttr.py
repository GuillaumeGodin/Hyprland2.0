#!/usr/bin/env python

import json
import requests
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

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

def get_weather(city):
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = session.get(f"https://wttr.in/{city}?format=j1", headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()

try:
    weather = get_weather(CITY)
except Exception as e:
    print(json.dumps({"text": "Err", "tooltip": str(e)}))
    exit()

def format_time(time):
    return time.replace("00", "").zfill(2)

def format_temp(temp):
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

# Current conditions logic (Fahrenheit)
curr_cond = weather['current_condition'][0]
tempint = int(curr_cond['FeelsLikeF'])
extrachar = ''
if 0 < tempint < 10:
    extrachar = '+'

# Output for Waybar
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
    elif i == 1:
        data['tooltip'] += "Tomorrow, "
    data['tooltip'] += f"{day['date']}</b>\n"
    data['tooltip'] += f"⬆️ {day['maxtempF']}° ⬇️ {day['mintempF']}° "
    data['tooltip'] += f"🌅 {day['astronomy'][0]['sunrise']} 🌇 {day['astronomy'][0]['sunset']}\n"
    for hour in day['hourly']:
        if i == 0:
            if int(format_time(hour['time'])) < datetime.now().hour - 2:
                continue
        data['tooltip'] += f"{format_time(hour['time'])} {WEATHER_CODES[hour['weatherCode']]} {format_temp(hour['FeelsLikeF'])} {hour['weatherDesc'][0]['value']}, {format_chances(hour)}\n"

print(json.dumps(data))