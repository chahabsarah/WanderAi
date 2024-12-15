
# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Voyage
from .forms import VoyageForm
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.db.models import Q
from reservation.models import Reservation
from Avis.forms import AvisForm
import datetime
from django.utils import timezone
from datetime import timedelta, datetime

# Create
@login_required

def voyage_create(request):
    if request.method == 'POST':
        form = VoyageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voyage-list')  # Rediriger vers la liste des voyages
    else:
        form = VoyageForm()
    return render(request, 'voyages/voyage_form.html', {'form': form})

# Read (List)
def voyage_list(request):
    continent = request.GET.get('continent')  
    if continent:
        voyages = Voyage.objects.filter(continent=continent)
    else:
        voyages = Voyage.objects.all()
    continents = [continent[0] for continent in Voyage.CONTINENTS]
    return render(request, 'voyages/voyage_list.html', {'voyages': voyages, 'continents': continents})


def search_voyages(request):
    query = request.GET.get('q', '').strip()  # Récupérer la requête et supprimer les espaces inutiles
    if query:
        # Recherche sur plusieurs champs avec Q objects
        voyages = Voyage.objects.filter(
            Q(nom__icontains=query) |
            Q(destination__icontains=query) |
            Q(date_depart__icontains=query) |
            Q(date_retour__icontains=query) |
            Q(prix__icontains=query)
        )
    else:
        # Si aucune requête, renvoyer tous les voyages
        voyages = Voyage.objects.all()
    
    voyages_list = list(voyages.values('nom', 'destination', 'date_depart', 'date_retour', 'prix'))
    return JsonResponse({'voyages': voyages_list})

def accueil(request):
    return render(request, 'voyages/accueil.html')

# Update
@login_required
def voyage_update(request, pk):
    voyage = get_object_or_404(Voyage, pk=pk)
    if request.method == 'POST':
        form = VoyageForm(request.POST, instance=voyage)
        if form.is_valid():
            form.save()
            return redirect('voyage-list') 
    else:
        form = VoyageForm(instance=voyage)
    return render(request, 'voyages/voyage_form.html', {'form': form})

# Delete
@login_required
def voyage_delete(request, pk):
    voyage = get_object_or_404(Voyage, pk=pk)
    if request.method == 'POST':
        voyage.delete()
        return redirect('voyage-list')  # Rediriger vers la liste des voyages
    return render(request, 'voyages/voyage_confirm_delete.html', {'voyage': voyage})
def voyage_detail(request, voyage_id):
    voyage = get_object_or_404(Voyage, id=voyage_id)

    avis = voyage.avis.all()
    context = {'voyage': voyage, 'avis': avis, 'voyage_id': voyage_id}

    return render(request, 'voyages/voyage_detail.html', context)


@login_required
def reserver_voyage(request, voyage_id):
    voyage = get_object_or_404(Voyage, id=voyage_id)

    # Vérifier si l'utilisateur a déjà réservé ce voyage
    if Reservation.objects.filter(user=request.user, voyage=voyage).exists():
        # Calculer la différence entre la date de départ et la date actuelle
        now = timezone.now().date()  # Convertir maintenant en date

        # Calculer la différence de temps
        time_diff = voyage.date_depart - now

        # Si la différence est supérieure à 24 heures, afficher le bouton annuler
        can_cancel = time_diff > timedelta(hours=24)

        return render(request, 'voyages/confirmation.html', {
            'message': f'Vous avez déjà réservé ce voyage pour {voyage.nom} à destination de {voyage.destination}.',
            'voyage': voyage,
            'can_cancel': can_cancel  # Passer la variable pour activer/désactiver le bouton
        })
    
    # Créer une nouvelle réservation
    reservation = Reservation(user=request.user, voyage=voyage)
    reservation.save()

    # Rediriger vers la page de confirmation
    return render(request, 'voyages/confirmation.html', {
        'message': f'Réservation réussie pour {voyage.nom} à destination de {voyage.destination}.',
        'voyage': voyage,
        'can_cancel': False  # Pas de possibilité d'annuler immédiatement après la réservation
    })

def avis_create(request, voyage_id):
    voyage = get_object_or_404(Voyage, id=voyage_id)
    
    user = request.user
    
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            avis = form.save(commit=False)
            avis.voyage = voyage
            avis.user = user  # Assigner l'instance User
            avis.save()
            return redirect('voyage_detail', voyage_id=voyage.id)  # Correction du paramètre pk
    else:
        form = AvisForm()

    return render(request, 'avis/avis_form.html', {'form': form, 'voyage': voyage})

