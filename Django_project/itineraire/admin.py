# itineraire/admin.py

from django.contrib import admin
from .models import Itineraire  # Assurez-vous que le modèle est importé

admin.site.register(Itineraire)  # Enregistrement du modèle
