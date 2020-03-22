from requests import get
import config
from chomsky.command import Command
from chomsky.number_to_text import NumberToText

class Weather(Command):
    id = 'weather'
    commands = None

    def run(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + config.WEATHER_CITY + '&units=metric&appid=' + config.WEATHER_API_KEY
        r = get(url)
        if r.status_code != 200:
            print('Error')
            return

        response = r.json()
        current_temp = NumberToText.convert(int(response['main']['temp']))
        feels_like = NumberToText.convert(int(response['main']['feels_like']))

        print('It is currently ' + current_temp + ' degrees')
        print('It feels like ' + feels_like)
        print(response)
