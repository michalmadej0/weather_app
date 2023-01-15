from django.shortcuts import render
import requests
from datetime import datetime
from babel.dates import format_datetime
import logging
# def home(request):
#
#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city = 'Łódź'
#
#     appid = 'a3c8518113db5c7bc4513414babcb42c'
#     URL ='https://api.openweathermap.org/data/2.5/weather'
#     PARAMS = {'q':city, 'appid':appid, 'units':'metric', 'lang':'pl'}
#     r = requests.get(url=URL, params=PARAMS)
#     res = r.json()
#     print(res)
#     description = res['weather'][0]['description']
#     icon = res['weather'][0]['icon']
#     temp = res['main']['temp'] #To add '°' press 'alt' + '0176'
#
#     day = format_datetime(datetime.now(), locale='pl')
#     return render(request, 'weather_app/home.html', {'description':description,
#                   'icon':icon, 'temp':temp, 'day':day,'city':city})

def home2(request):
    try:
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

        return render(request,'weather_app/home2.html',
                      {'temp': temp, 'description':description,
                       'icon':icon, 'city2':city2,'day':day, 'pressure':pressure})
    except:
            return render(request,'weather_app/error.html')
