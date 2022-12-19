import requests
import json
from pprint import pprint
city = 'Moscow'
api_key='0338b07571945f05e7b068ddad51fc53'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url).json()

pprint(
    f'В городе {response.get("name")} температура {response.get("main").get("temp") - 273.15} градусов')

with open("data_weather.json", "w") as f:
    json.dump(response,f)

