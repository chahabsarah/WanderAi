# forms.py
from django import forms
from .models import Voyage


class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = ['nom', 'destination', 'date_depart', 'date_retour', 'prix', 'continent','duration','travel_mode']
