from django.core.management.base import BaseCommand
import schedule
import time
import requests
import datetime
from .models import Weather


class Command(BaseCommand):
    help = 'Update weather data'

    def handle(self):
        def job():
            url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            city = 'Warsaw'
            api_key = 'a3c8518113db5c7bc4513414babcb42c'
            response = requests.get(url.format(city=city, api_key=api_key)).json()
            temperature = response['main']['temp']
            date = datetime.now()
            Weather.objects.create(temperature=temperature, date=date)
            self.stdout.write(self.style.SUCCESS('Successfully update weather data'))

        schedule.every(2).minutes.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)