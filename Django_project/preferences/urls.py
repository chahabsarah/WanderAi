# urls.py
from django.urls import path
from .views import preference_create, preference_list, preference_update, preference_delete

urlpatterns = [
    path('', preference_list, name='preference-list'),
    path('create/', preference_create, name='preference-create'),
    path('update/<int:pk>/', preference_update, name='preference-update'),
    path('delete/<int:pk>/', preference_delete, name='preference-delete'),
]
