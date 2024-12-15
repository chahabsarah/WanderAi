from django.urls import path
from .views import  AvisUpdateView, AvisDeleteView

urlpatterns = [
    path('update/<int:pk>/', AvisUpdateView.as_view(), name='avis-update'),
    path('delete/<int:pk>/', AvisDeleteView.as_view(), name='avis-delete'),
]
