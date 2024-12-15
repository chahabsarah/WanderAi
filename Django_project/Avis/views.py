# avis/views.py
from django.views import generic
from .forms import AvisForm  # Assurez-vous de créer un formulaire pour Avis
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Voyage, Avis
from preferences.models import UserProfile


@login_required




def avis_list(request, voyage_id):
    voyage = get_object_or_404(Voyage, id=voyage_id)
    avis = voyage.avis.all()
    return render(request, 'avis/avis_list.html', {'voyage': voyage, 'avis': avis},)


class AvisUpdateView(generic.UpdateView):
    model = Avis
    form_class = AvisForm
    template_name = 'avis/avis_edit.html'
    success_url = reverse_lazy('avis-list')

class AvisDeleteView(generic.DeleteView):
    model = Avis
    template_name = 'avis/avis_confirm_delete.html'
    success_url = reverse_lazy('avis-list')
