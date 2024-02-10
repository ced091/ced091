from django.urls import path, include
from . import views

app_name='docs'

urlpatterns = [
    path('documentation/<path:path>', views.main, name="main"),
]