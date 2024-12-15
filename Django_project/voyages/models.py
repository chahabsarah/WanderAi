from django.db import models
from django.conf import settings

# models.py
class Voyage(models.Model):
    CONTINENTS = [
        ('Afrique', 'Afrique'),
        ('Antarctique', 'Antarctique'),
        ('Asie', 'Asie'),
        ('Europe', 'Europe'),
        ('Amérique du Nord', 'Amérique du Nord'),
        ('Océanie', 'Océanie'),
        ('Amérique du Sud', 'Amérique du Sud'),
    ]
    nom = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_depart = models.DateField()
    date_retour = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    travel_type = models.CharField(max_length=50,default="Non spécifié")
    continent = models.CharField(max_length=100, default="Non spécifié")
    duration = models.CharField(max_length=50,default="Non spécifié")
    travel_mode = models.CharField(max_length=20,default="Non spécifié")
    def __str__(self):
        return f"Voyage {self.nom} à {self.destination}"
