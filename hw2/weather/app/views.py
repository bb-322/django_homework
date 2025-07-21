import requests
import os
from dotenv import load_dotenv 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

load_dotenv()
API_KEY = os.getenv('WEATHER_KEY')

class Page(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get('city', '').strip()
        if city:
            weather_dict = get_weather_dict(city=city)
            if weather_dict["cod"] != 200:
                context['alert'] = f'<script>alert("City {city} does not exist!");</script>'
            else:
                context['country'] = weather_dict['sys']['country']
                context['city'] = weather_dict['name']
                context['lon'] = weather_dict['coord']['lon']
                context['lat'] = weather_dict['coord']['lat']
                context['weather'] = weather_dict['weather'][0]['main']
                context['temp'] = weather_dict['main']['temp']
        else: 
            context['alert'] = f'''<script>alert("broski, enter city using ?city=*your city*");</script>'''
        return context

def get_weather_dict(city=str) -> dict:
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric'
    response = requests.get(weather_api)
    return response.json()