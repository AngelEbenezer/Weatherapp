# weather_app/views.py
from django.shortcuts import render
import requests

def weather(request):
    api_key = '2439126a79ae7d0e9a6f4d44cdd7b8c6'
    city = request.GET.get('city', 'Bangalore')  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'city': city,
        }
    else:
        weather_data = {
            'error': 'City not found or API error'
        }

    context = {'weather_data': weather_data}
    return render(request, 'weather/weather.html', context)


