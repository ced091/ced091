from django.urls import path

from . import views

app_name = 'station_meteo'

urlpatterns = [
    path('', views.accueil, name='accueil'),
]