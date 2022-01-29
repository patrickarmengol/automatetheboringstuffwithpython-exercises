import json, requests, sys

APPID = '__FILLME__'

if len(sys.argv) < 2:
    print('usage: getopenweather.py city_name country_code')
    sys.exit()

city_name = ' '.join(sys.argv[1:-1])
country_code = sys.argv[-1]

# daily forecast api is no longer supported under free plan; i'll do current weather instead
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&units=metric&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

# print(response.text)

weather_data = json.loads(response.text)
# print(weather_data)

sky = weather_data['weather'][0]['description']
temp = weather_data['main']['temp']
feels = weather_data['main']['feels_like']
wind_speed = weather_data['wind']['speed']
wind_dir = weather_data['wind']['deg']

print(f'sky: {sky}')
print(f'temp: {temp} C (feels like {feels} C)')
print(f'wind: {wind_speed} m/s at {wind_dir} deg')
