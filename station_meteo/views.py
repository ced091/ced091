from django.shortcuts import render
from django.http import HttpResponse

from station_meteo.models import Bme280

# Create your views here.

from datetime import datetime

def accueil(request):
    x= Bme280.objects.all()
    y= Bme280.objects.all()
    data_hum = []
    data_temp= []
    data_press=[]
    for i in range(0,20):
        data_hum.append({'x': (x[i].date_point)*1000, 'y': y[i].pression})
    for i in range(0,len(x)):
        data_press.append({'x': (x[i].date_point)*1000, 'y': y[i].humidity})
    for i in range(0,len(x)):
        data_temp.append({'x': (x[i].date_point)*1000, 'y': y[i].temp})
    return render(request, 'station_meteo/accueil.html', {'data_hum': data_hum, 'data_temp': data_temp, 'data_press': data_press,})
