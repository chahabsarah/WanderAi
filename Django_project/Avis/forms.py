# avis/forms.py
from django import forms
from .models import Avis

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['note', 'commentaire']

    def __init__(self, *args, **kwargs):
        super(AvisForm, self).__init__(*args, **kwargs)
