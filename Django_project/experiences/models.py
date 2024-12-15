

from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='experiences/', null=True, blank=True)  # Ajouter ce champ

    def __str__(self):
        return self.title

class UserReaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'J\'aime'),
        ('dislike', 'Je n\'aime pas'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=7, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'experience')  # Assure que chaque utilisateur ne peut choisir qu'une seule option par expérience
