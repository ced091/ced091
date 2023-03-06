import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ced091.settings')
django.setup()

from .models import Bme280
from .capteur_temp import reading_data

def save_data():
    data = reading_data()
    timestamp = float(data.timestamp.timestamp())
    temperature = float(data.temperature)
    pression = float(data.pressure)
    humidity = float(data.humidity)
    point = Bme280(date_point = timestamp, temp = temperature, humidity = humidity, pression = pression)
    point.save()