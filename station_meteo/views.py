import logging

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
import pytz

from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def log_user(request, vue):
    username = request.user.username if request.user.is_authenticated else 'Anonymous'
    current_datetime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if ip_address is None:
        # Si l'en-tête X-Forwarded-For n'est pas disponible, utilisez l'adresse IP par défaut
        ip_address = request.META.get('REMOTE_ADDR', 'unknown')
    else:
        # Séparez les adresses IP si X-Forwarded-For contient plusieurs adresses
        ip_address = ip_address.split(",")[0].strip()
    logger.info(f'[{current_datetime}][{username}][{ip_address}] Accès à la vue {vue}')

class MeteoPointAPIView(APIView):
    def post(self, request):
        serializer = MeteoPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

def accueil(request):
    log_user(request, "accueil/meteo")
    last_24_hours = timezone.now() - timedelta(hours=24)
    data = MeteoPoint.objects.filter(timestamp__gte=last_24_hours)
    # Préparer les données pour le passage au template
    paris_tz = pytz.timezone("Europe/Paris")
    labels = [entry.timestamp.astimezone(paris_tz).strftime("%Y-%m-%d %H:%M:%S") for entry in data]
    temperature = [entry.temperature for entry in data]
    max_temperature = "{:.3f}".format(max(temperature))
    min_temperature = "{:.3f}".format(min(temperature))
    avg_temperature = "{:.3f}".format(sum(temperature)/len(temperature))
    st_dev_temperature = "{:.3f}".format(stdev(temperature))
    pressure = [entry.pressure for entry in data]
    max_pressure = "{:.3f}".format(max(pressure))
    min_pressure = "{:.3f}".format(min(pressure))
    avg_pressure = "{:.3f}".format(sum(pressure)/len(pressure))
    st_dev_pressure = "{:.3f}".format(stdev(pressure))
    humidity = [entry.humidity for entry in data]
    max_humidity = "{:.3f}".format(max(humidity))
    min_humidity = "{:.3f}".format(min(humidity))
    avg_humidity = "{:.3f}".format(sum(humidity)/len(humidity))
    st_dev_humidity = "{:.3f}".format(stdev(humidity))
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

