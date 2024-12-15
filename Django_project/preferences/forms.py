# forms.py
from django import forms
from .models import Preference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['travel_type','budget','duration','preferred_destination','preferred_period', 'travel_mode']

    def __init__(self, *args, **kwargs):
        # Récupérer l'utilisateur connecté à partir des kwargs
        self.user = kwargs.pop('user', None)
        super(PreferenceForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        preference = super(PreferenceForm, self).save(commit=False)
        if self.user:  # Assurez-vous que l'utilisateur est défini
            preference.user = self.user
        if commit:
            preference.save()
        return preference
