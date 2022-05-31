from intent_functions.locator import Locator
import requests
import intent_classification.intent_tts as tts
import config



api_key = config.weather_api_key


def determine_weather():
    # using locator.py to determine users position
    lat = Locator.lat
    long = Locator.long

    # locating the city
    city = Locator.city

    url = f'https://api.weatherbit.io/v2.0/current?&lat={lat}&lon={long}&key={api_key}&units=I'

    # gathering the response from the api request
    response = requests.get(url)

    # gathering the data from the json file
    data = response.json()['data'][0]

    # putting the data into variables
    date = data['datetime']
    weather_desc = data['weather']['description']
    temp = data['temp']
    uv = data['uv']
    dewpt = data['dewpt']
    rh = data['rh']
    realfeel = data['app_temp']
    precip = data['precip']
    wind_speed = data['wind_spd']
    wind_dir = data['wind_cdir_full']

    # printing the main weather data
    message = (
        f"In the city of {city}, the temperature is {temp} degrees Fahrenheit with a real feel of {realfeel} degrees "
        f"fahrenheit. "
        f"The precipitation is {precip}. "
        f"The wind speed is currently {wind_speed} miles per hour {wind_dir}")

    tts.say(message)


    # printing additional weather data upon user request
    tts.say("Would you like a detailed breakdown of the weather? ")
    answer = tts.listen()

    answer = answer.lower()
    if answer == "yes":
        message = (f"The weather is currently described as {weather_desc}. "
                   f"The dew point is {dewpt} degrees fahrenheit. "
                   f"The humidity is {rh} percent."
                   f"The UV index is {uv}.")
        tts.say(message)
