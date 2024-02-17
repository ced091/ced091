from django.db import models

# Create your models here.

class Bme280(models.Model):
    date_point = models.FloatField(null=False)
    temp = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    pression = models.FloatField(null=False)

    def __str__(self):
        return str(self.date_point) + "," + str(self.temp) + "," + str(self.humidity) + "," + str(self.pression)
    
class MeteoPoint(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp + " " +
                   str(self.temperature) + " " +
                   str(self.humidity) + " " +
                   str(self.timestamp))
