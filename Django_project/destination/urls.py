from django.urls import path
from . import views

app_name = 'destination'  # Namespace for the destination app

urlpatterns = [
    path('', views.destination_list, name='list'),  # List all destinations
    path('create/', views.destination_create, name='create'),  # Create a new destination
    path('<int:pk>/update/', views.destination_update, name='update'),  # Update a destination
    path('<int:pk>/delete/', views.destination_delete, name='delete'),  # Delete a destination
]
