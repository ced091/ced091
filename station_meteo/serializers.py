# serializers.py
from rest_framework import serializers
from .models import MeteoPoint

class MeteoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeteoPoint
        fields = ['temperature', 'humidity', 'pressure', 'timestamp']
