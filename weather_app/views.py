from django.shortcuts import render
import requests
from datetime import datetime
from babel.dates import format_datetime
from .models import Weather

def home(request):
        if request.method == 'POST':
            city = request.POST.get('city')
        else:
            city = 'Łódź'

        api_key = 'a3c8518113db5c7bc4513414babcb42c'
        lang = 'pl'
        units = 'metric'
        day = format_datetime(datetime.now(), locale='pl')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}' \
              f'&lang={lang}'
        response = requests.get(url).json()
        try:
            temp = response['main']['temp']
            description = response['weather'][0]['description']
            icon = response['weather'][0]['icon']
            pressure = response['main']['pressure']
        except KeyError:
            description = 'Wprowadz poprawne dane'
            return render(request, 'weather_app/key_error.html',
                          {'description': description,
                             'city': city, 'day': day})

        weather = Weather(city=city, temp=temp, pressure=pressure, )
        weather.save()

        return render(request,'weather_app/home2.html',
                      {'temp': temp, 'description':description,
                       'icon':icon, 'city':city,'day':day, 'pressure':pressure})
def load_date(request):
    if request.method == 'POST':
        weather_data = request.FILES.get('weather_data')
        response = requests.get(weather_data, stream=True)
        with open('temp/weather_data.csv', 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        with open('temp/weather_data.csv', newline='') as f:
            csv_str = f.read()
        return render(request, 'weather_app/success.html', {'weather_data':weather_data, 'csv_str':csv_str})

    return render(request, 'weather_app/load_data.html')
