# itineraire/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Itineraire
from destination.models import Destination  # Assure-toi d'importer le modèle Destination

# List View
def itineraire_list(request):
    itineraries = Itineraire.objects.filter(utilisateur=request.user)
    return render(request, 'itineraire/itineraire_list.html', {'itineraries': itineraries})

# Create View
def itineraire_create(request):
    if request.method == 'POST':
        utilisateur = request.user  # Assuming the user is logged in
        destination_id = request.POST['destination']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        preferences = request.POST.get('preferences', '')

        destination = Destination.objects.get(id=destination_id)
        Itineraire.objects.create(
            utilisateur=utilisateur,
            destination=destination,
            date_debut=date_debut,
            date_fin=date_fin,
            preferences=preferences
        )
        return redirect('itineraire:list')  # Redirect to itinerary list after creation

    destinations = Destination.objects.all()  # Fetch all destinations to pass to the template
    return render(request, 'itineraire/itineraire_create.html', {'destinations': destinations})

# Update View
def itineraire_update(request, pk):
    itineraire = get_object_or_404(Itineraire, pk=pk)
    
    if request.method == 'POST':
        itineraire.destination_id = request.POST['destination']
        itineraire.date_debut = request.POST['date_debut']
        itineraire.date_fin = request.POST['date_fin']
        itineraire.preferences = request.POST.get('preferences', '')
        itineraire.save()
        return redirect('itineraire:list')  # Redirect to itinerary list after update

    destinations = Destination.objects.all()  # Fetch all destinations to pass to the template
    return render(request, 'itineraire/itineraire_update.html', {'itineraire': itineraire, 'destinations': destinations})

# Delete View
def itineraire_delete(request, pk):
    itineraire = get_object_or_404(Itineraire, pk=pk)
    
    if request.method == 'POST':
        itineraire.delete()
        return redirect('itineraire:list')  # Redirect to itinerary list after deletion

    return render(request, 'itineraire/itineraire_delete.html', {'itineraire': itineraire})
