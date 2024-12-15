# itineraire/models.py
from django.db import models
from django.contrib.auth.models import User
from destination.models import Destination  # Assure-toi d'importer le modèle Destination

class Itineraire(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Itinéraire de {self.utilisateur.username} vers {self.destination.nom}"
