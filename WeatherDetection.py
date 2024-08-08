import requests
import json

# API key
city_name=input("Enter the city name:")
API_key="ef804fc2cad1f7855188c81d9e70ef84"
lang="hi"

# API url
API_url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
Get_Server_info=requests.get(API_url)
x=Get_Server_info.json()
y = x["main"]
current_temperature = y["temp"]
print("Temperature:",current_temperature)
Humidity= y["humidity"]
print("Humidity:",Humidity)
y = x["wind"]
Wind_speed= y["speed"]
print("Wind speed:",Wind_speed)

