from django.urls import path

from . import views
from . import ajax

app_name = 'station_meteo'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('add_bme280/', views.add_bme280, name='add_bme280'),
    path('refresh_data/', ajax.refresh_data, name="refresh_data"),
]