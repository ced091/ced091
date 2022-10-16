from django.db import models

# Create your models here.

class Bme280(models.Model):
    date_point = models.FloatField(null=False)
    temp = models.FloatField(null=False)
    humidity = models.FloatField(null=False)
    pression = models.FloatField(null=False)

    def __str__(self):
        return str(self.date_point) + "," + str(self.temp) + "," + str(self.humidity) + "," + str(self.pression)
