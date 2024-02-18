from statistics import stdev

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MeteoPoint
from .serializers import MeteoPointSerializer

from django.shortcuts import render, redirect
from django.http import HttpResponse

from station_meteo.models import Bme280
from .forms import Bme280Form
from .capteur_temp import reading_data

# Create your views here.

from django.utils import timezone

from datetime import datetime, timedelta

# def accueil(request):
#     x= Bme280.objects.all()
#     y= Bme280.objects.all()
#     data_hum = []
#     data_temp= []
#     data_press=[]
#     try :
#         data = reading_data()
#         context = {
#         "temp_now": round(data.temperature,2),
#         "pression_now": round(data.pressure,2),
#         "humidity_now": round(data.humidity,2),
#         }
#     except:
#         context = {}    
#     try : 
#         for i in range(0,len(x)):
#             data_hum.append({'x': datetime.fromtimestamp(x[i].date_point).strftime('%m/%d/%Y %H:%M:%S'), 'y': y[i].humidity})
#         for i in range(0,len(x)):
#             data_press.append({'x': datetime.fromtimestamp(x[i].date_point).strftime('%m/%d/%Y %H:%M:%S'), 'y': y[i].pression})
#         for i in range(0,len(x)):
#             data_temp.append({'x': datetime.fromtimestamp(x[i].date_point).strftime('%m/%d/%Y %H:%M:%S'), 'y': y[i].temp})
#     except:
#         pass
#     context['data_hum'] = data_hum
#     context['data_temp'] = data_temp
#     context['data_press'] = data_press
#     return render(request, 'station_meteo/accueil.html', context)



def add_bme280(request):
    data = reading_data()
    date_object = data.timestamp.timestamp()
    timestamp = float(date_object)
    initial_data = {'temp': data.temperature, 'humidity': data.humidity, 'pression': data.pressure, 'date_point': timestamp}
    if request.method == 'POST':
        form = Bme280Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('station_meteo:accueil')
    else:
        form = Bme280Form(initial=initial_data)

    return render(request, 'station_meteo/add_bme280.html', {'form': form})

class MeteoPointAPIView(APIView):
    def post(self, request):
        serializer = MeteoPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def accueil(request):
    last_24_hours = timezone.now() - timedelta(hours=24)
    data = MeteoPoint.objects.filter(timestamp__gte=last_24_hours)
    # Préparer les données pour le passage au template
    labels = [entry.timestamp.strftime("%Y-%m-%d %H:%M:%S") for entry in data]
    temperature = [entry.temperature for entry in data]
    max_temperature = "{:.3f}".format(max(temperature)) + " °C"
    min_temperature = "{:.3f}".format(min(temperature)) + " °C"
    avg_temperature = "{:.3f}".format(sum(temperature)/len(temperature)) + " °C"
    st_dev_temperature = "{:.3f}".format(stdev(temperature)) + " °C"
    pressure = [entry.pressure for entry in data]
    max_pressure = "{:.3f}".format(max(pressure)) + " hPa"
    min_pressure = "{:.3f}".format(min(pressure)) + " hPa"
    avg_pressure = "{:.3f}".format(sum(pressure)/len(pressure)) + " hPa"
    st_dev_pressure = "{:.3f}".format(stdev(pressure)) + " hPa"
    humidity = [entry.humidity for entry in data]
    max_humidity = "{:.3f}".format(max(humidity)) + " %"
    min_humidity = "{:.3f}".format(min(humidity)) + " %"
    avg_humidity = "{:.3f}".format(sum(humidity)/len(humidity)) + " %"
    st_dev_humidity = "{:.3f}".format(stdev(humidity)) + " %"
    context = {
        'labels': labels,
        'temperature': temperature,
        'pressure' : pressure,
        'humidity' : humidity,
        'max_temperature' : max_temperature,
        'min_temperature' : min_temperature,
        'avg_temperature' : avg_temperature,
        'st_dev_temperature' : st_dev_temperature,
        'max_pressure' : max_pressure,
        'min_pressure' : min_pressure,
        'avg_pressure' : avg_pressure,
        'st_dev_pressure' : st_dev_pressure,
        'max_humidity' : max_humidity,
        'min_humidity' : min_humidity,
        'avg_humidity' : avg_humidity,
        'st_dev_humidity' : st_dev_humidity,
    }
    return render(request, 'station_meteo/accueil_bis.html', context)

