from django import forms
from .models import Bme280

class Bme280Form(forms.ModelForm):
    class Meta:
        model = Bme280
        fields = ['date_point', 'temp', 'humidity', 'pression']