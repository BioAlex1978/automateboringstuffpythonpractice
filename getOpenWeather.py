#! python3

# getOpenWeather.py - a program that takes a location as a command line argument and
# gets current and upcoming weather from OpenWeatherMap.org and prints it to the screen
# Automate the Boring Stuff with Python 2e, chapter 16, pg.383

# NOTE: the URL provided by the book is no longer freely accessible, so instead I have modified
# this to use the OpenWeatherMap OneCall API to get the current weather and daily forecasts

# in order to work, you need an app ID from OpenWeatherMap.org/api
APPID = 'YOUR_APPID_HERE'

import json, requests, sys

# compute Location from command line arguments
if len(sys.argv) < 2:
    print('Usage: ')
    print('getOpenWeather.py city_name, 2-letter_state_code(optional), 2-letter_country_code')
    print('--or--')
    print('getOpenWeather.py ZIP_code, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:]) # joins the location arguments as a string separated by spaces

# NOTE: The following is what the book wanted to do, but that API is no longer freely accessible
# download the JSON data from OpenWeatherMap.org's API
#url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&APPID={APPID} '
#response = requests.get(url)
#response.raise_for_status()


# to use OneCall, we need the lat and lon coordintes. We can get that from making a call to the current weather API
# there's possibly a more efficient way to do this, but this works for me
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

# get the coordinates
coordsData = json.loads(response.text)
lat = coordsData['coord']['lat']
lon = coordsData['coord']['lon']

# use the coordinates from the previous call to make a call to the OneCall API to get the forecast
# we don't want minutely or hourly data, so we can exclude them to reduce the amount of data downloaded
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

# NOTE: the weather data returned is formatted differently from the book's example. In the book, everything
# was under the key 'list'. For OneCall, 'current' is its own key, and then the 'daily' key is a list
# with ['daily'][0] being the entry for tomorrow and so on
weatherData = json.loads(response.text)
print(f'Current weather in {location}:')
print(weatherData['current']['weather'][0]['main'] + ' - ' + weatherData['current']['weather'][0]['description'])
print()
daily = weatherData['daily']
print('Tomorrow:')
print(daily[0]['weather'][0]['main'] + ' - ' + daily[0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(daily[1]['weather'][0]['main'] + ' - ' + daily[1]['weather'][0]['description'])
print()
