# urls.py
from django.urls import path
from . import views
from reservation.views import mes_reservations

urlpatterns = [
   
    path('mes_reservations/', views.mes_reservations, name='mes_reservations'),  # URL pour les réservations de l'utilisateur
    path('annuler_reservation/<int:reservation_id>/', views.annuler_reservation, name='annuler_reservation'),  # URL pour annuler une réservation

]
