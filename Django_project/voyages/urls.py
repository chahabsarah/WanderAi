# urls.py
from django.urls import path
from . import views

from voyages.views import voyage_detail, avis_create
urlpatterns = [
    path('', views.voyage_list, name='voyage-list'),
    path('create/', views.voyage_create, name='voyage-create'),
    path('update/<int:pk>/', views.voyage_update, name='voyage-update'),
    path('delete/<int:pk>/', views.voyage_delete, name='voyage-delete'),
    path('accueil/', views.accueil, name='accueil'),
    path('search/', views.search_voyages, name='search-voyages'),
    path('<int:voyage_id>/details/', voyage_detail, name='voyage_detail'),
    path('<int:voyage_id>/reserver/', views.reserver_voyage, name='reserver_voyage'),
    path('<int:voyage_id>/ajouterAvis/', avis_create, name='avis-create'),
    


]
