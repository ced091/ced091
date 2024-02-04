from django.urls import path

from . import views

app_name = 'libeiki'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('reiki/', views.reiki, name='reiki'),
    path('quisuisje/', views.quisuisje, name='quisuisje'),
    path('massage-visage/', views.visage, name='visage'),
    path('sophrologie/', views.sophrologie, name='sophrologie'),
    path('numerologie/', views.numerologie, name='numerologie'),
    path('lignee-reiki/', views.lignee_reiki, name="lignee_reiki"),
    path('contact/', views.contact, name='contact'),
    path('tarif-reiki/', views.tarif_reiki, name='tarif_reiki'),
    path('tarif-numerologie/', views.tarif_numerologie, name='tarif_numerologie'),
    path('send-commentaire/', views.send_commentaire, name='send_commentaire'),
]