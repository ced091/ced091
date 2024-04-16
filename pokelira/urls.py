from django.urls import path

from . import views

app_name = 'pokelira'

urlpatterns = [
    path("", views.accueil, name="accueil"),
]