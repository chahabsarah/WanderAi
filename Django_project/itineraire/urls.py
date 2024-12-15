# itineraire/urls.py
from django.urls import path
from . import views

app_name = 'itineraire'  # Namespace for the itineraire app

urlpatterns = [
    path('', views.itineraire_list, name='list'),  # List all itineraries
    path('create/', views.itineraire_create, name='create'),  # Create a new itinerary
    path('<int:pk>/update/', views.itineraire_update, name='update'),  # Update an itinerary
    path('<int:pk>/delete/', views.itineraire_delete, name='delete'),  # Delete an itinerary
]
