from django.db import models
from django.utils import timezone

# Create your models here.

class Commentaire(models.Model):
    pseudo = models.CharField(max_length=50)
    note = models.IntegerField()
    texte = models.TextField()
    date_com = models.DateField(default=timezone.now)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return "Com' de " + str(self.pseudo)
    
    class Meta:
        ordering = ['-date_com']