from django.shortcuts import render
import requests
from datetime import datetime
from babel.dates import format_datetime
from .models import Weather


def home2(request):
        if 'city2' in request.POST:
            city2 = request.POST['city2']
        else:
            city2 = 'Łódź'

        api_key = 'a3c8518113db5c7bc4513414babcb42c'
        lang = 'pl'
        units = 'metric'
        day = format_datetime(datetime.now(), locale='pl')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city2}&appid={api_key}&units={units}' \
              f'&lang={lang}'
        response = requests.get(url).json()
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        icon = response['weather'][0]['icon']
        pressure = response['main']['pressure']

        weather = Weather(city=city2, temp=temp, pressure=pressure, )
        weather.save()

        return render(request,'weather_app/home2.html',
                      {'temp': temp, 'description':description,
                       'icon':icon, 'city2':city2,'day':day, 'pressure':pressure})

