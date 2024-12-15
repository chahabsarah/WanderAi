from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Preference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travel_type = models.CharField(max_length=50,default="Non spécifié")
    budget =  models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50,default="Non spécifié")
    preferred_destination = models.CharField(max_length=100, default="Non spécifié")
    preferred_period = models.CharField(max_length=20 ,default="Non spécifié")
    travel_mode = models.CharField(max_length=20,default="Non spécifié")
def __str__(self):
    return f"{self.user.name} - {self.travel_type} - {self.budget} - {self.duration} - {self.preferred_destination}"
