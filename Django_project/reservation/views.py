from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from reservation.models import Reservation
from voyages.models import Voyage
from django.contrib.auth.decorators import login_required
import datetime


@login_required

def mes_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    now = timezone.now().date()

    # Vérifier si chaque réservation peut être annulée
    for reservation in reservations:
        voyage = reservation.voyage
        time_diff = voyage.date_depart - now
        reservation.can_cancel = time_diff > timedelta(hours=24)

    return render(request, 'reservation/mes_reservations.html', {'reservations': reservations})
@login_required

def annuler_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    voyage = reservation.voyage

    # Vérifier si la réservation peut être annulée
    now = timezone.now()

    # Si voyage.date_depart est de type date, convertir maintenant en date
    if isinstance(voyage.date_depart, datetime.date):
        now = now.date()  # Convertir maintenant en date

    # Calculer la différence de temps
    time_diff = voyage.date_depart - now

    if time_diff > timedelta(hours=24):
        # Annuler la réservation
        reservation.delete()
        return render(request, 'voyages/confirmation.html', {
            'message': 'Votre réservation a été annulée.',
        })
    else:
        return render(request, 'voyages/confirmation.html', {
            'message': 'Impossible d\'annuler la réservation car la date de départ est inférieure à 24 heures.',
        })