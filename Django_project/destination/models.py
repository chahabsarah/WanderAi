# destination/models.py
from django.db import models

class Destination(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)

    def __str__(self):
        return self.nom
