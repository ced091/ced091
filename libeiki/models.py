from django.db import models

# Create your models here.

class Commentaire(models.Model):
    pseudo = models.CharField(max_length=50)
    note = models.FloatField()
    texte = models.TextField()

    def __str__(self):
        return "Com' de " + str(self.pseudo)