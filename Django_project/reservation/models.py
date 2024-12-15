from django.db import models

# Create your models here.
from django.conf import settings
from voyages.models import Voyage

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réservation de {self.user} pour le voyage {self.voyage.nom}"
