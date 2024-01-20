from django.urls import path

from . import views

app_name = 'libeiki'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('reiki/', views.reiki, name='reiki'),
    path('quisuisje/', views.quisuisje, name='quisuisje'),
    path('massage-visage/', views.visage, name='visage'),
    path('sophrologie/', views.sophrologie, name='sophrologie'),
]