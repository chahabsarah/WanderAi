from django.db import models
#model avis
# Create your models here.
from django.conf import settings

from preferences.models import UserProfile
from voyages.models import Voyage
class Avis(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='avis')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=0)  # Note de 1 à 5
    commentaire = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis de {self.user.username} pour {self.voyage.nom} - Note: {self.note}"  # Use user.username

