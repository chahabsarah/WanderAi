from django.db import models
from preferences.models import UserProfile

# Model pour les Recommandations (Recommendation)
class Recommendation(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recommendations')
    experience_name = models.CharField(max_length=200, default='Expérience non spécifiée')  # Valeur par défaut ajoutée
    date_recommended = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.experience_name}"
