from django.shortcuts import render, redirect
from django.http import HttpResponse

from station_meteo.models import Bme280
from .forms import Bme280Form
from capteur_temp import reading_data

# Create your views here.

from datetime import datetime

def accueil(request):
    x= Bme280.objects.all()
    y= Bme280.objects.all()
    data_hum = []
    data_temp= []
    data_press=[]
    for i in range(0,20):
        data_hum.append({'x': datetime.fromtimestamp(x[i].date_point).strftime('%m/%d/%Y %H:%M:%S'), 'y': y[i].pression})
    for i in range(0,len(x)):
        data_press.append({'x': datetime.fromtimestamp(x[i].date_point).strftime('%m/%d/%Y %H:%M:%S'), 'y': y[i].humidity})
    for i in range(0,len(x)):
        data_temp.append({'x': datetime.fromtimestamp(x[i].date_point).strftime('%m/%d/%Y %H:%M:%S'), 'y': y[i].temp})
    return render(request, 'station_meteo/accueil.html', {'data_hum': data_hum, 'data_temp': data_temp, 'data_press': data_press,})

def add_bme280(request):
    data = reading_data()
    initial_data = {'temp': data.temperature, 'humidity': data.humidity, 'pression': data.pression, 'date_point': data.timestamp}
    if request.method == 'POST':
        print(request.POST)
        form = Bme280Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = Bme280Form(initial=initial_data)

    return render(request, 'station_meteo/add_bme280.html', {'form': form})
