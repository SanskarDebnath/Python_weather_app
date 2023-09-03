import datetime as dt
import requests
BASE_URl = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api.txt', 'r').read()
city = str(input("Enter the City name : "))
def kelvin_cel_fahrenhite(temp_k):
    c = temp_k - 273.15
    f = c * (9/5) + 32
    return c, f
url = BASE_URl+"appid="+API_KEY+"&q="+city
response = requests.get(url).json()
temp_k = response['main']['temp']
temp_c, temp_f = kelvin_cel_fahrenhite(temp_k)
feels_like_k = response['main']['feels_like']
feels_like_c , feels_like_f = kelvin_cel_fahrenhite(feels_like_k)
windspeed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sun_rise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sun_set_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
print(f"Tempreture In city {city} : {temp_c : .2f}°C or {temp_f}°F")
print(f"Tempreture In city {city} Feels like : {feels_like_c : .2f}°C or {feels_like_f}°F")
print(f"Wind Speed In city {city} : {windspeed} M/S")
print(f"General weather in city {city} : {description}")
print(f"Sun rises time in city {city} at {sun_rise_time} local time.")
print(f"Sun sets time in city {city} at {sun_set_time} local time.")