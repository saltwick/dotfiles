#!/bin/python
import pywapi
import json
import requests

#Define units - 'imperial' or 'metric'
UNITS = 'imperial'

#Define variables for weather icons

SUNNY = "  "
RAIN = "  "
CLOUD = "  "
FAIR = ""
WIND = " | "
LOW_TEMP = "  "
MED_TEMP = "  "
HIGH_TEMP = "  "

#Get the geolocation of your IP address through freegeoip.net
loc_url = 'http://freegeoip.net/json'
req = requests.get(loc_url)
json_request = json.loads(req.text)

#Pull the zip code from the json 
zip_code = json_request['zip_code']

#Use pywapi and weather.com to get the current weather
weather = pywapi.get_weather_from_weather_com(json_request['zip_code'], UNITS)

#Get units
speed_unit_string = weather['units']['speed']
temp_unit_string = "°" + weather['units']['temperature']

#Change the temperature icon based on the current temperature
temp_icon = ""
temp_val = int(weather['current_conditions']['temperature'])
if temp_val < 40:
    temp_icon = LOW_TEMP
elif temp_val >= 40 and temp_val < 70:
    temp_icon = MED_TEMP
else:
    temp_icon = HIGH_TEMP

#Choose a weather icon based on current conditions
icon =  weather['current_conditions']['text'].lower()
if "cloud" in icon:
    icon = CLOUD
elif "rain" in icon:
    icon = RAIN
elif "sun" in icon or "fair" in icon:
    icon = SUNNY
elif "partly cloudly" in icon:
    icon = CLOUD + SUNNY

#Change text if the wind speed is "calm"
wind_string = ""
if weather['current_conditions']['wind']['speed'] == "calm":
    wind_string = "Calm Winds"
else:
    wind_string = weather['current_conditions']['wind']['speed'] + speed_unit_string

print(icon + " | " + temp_icon + " " + str(temp_val)+ temp_unit_string + WIND  + wind_string)
