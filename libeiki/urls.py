from django.urls import path

from . import views

app_name = 'libeiki'

urlpatterns = [
    path('', views.accueil, name='accueil'),
]