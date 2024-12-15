# urls.py
from django.urls import path
from .views import experience_create, experience_list, experience_update, experience_delete
from experiences import views


urlpatterns = [
    path('', experience_list, name='experience-list'),
    path('create/', experience_create, name='experience-create'),
    path('update/<int:pk>/', experience_update, name='experience-update'),
    path('delete/<int:pk>/', experience_delete, name='experience-delete'),
    path('reaction/<int:experience_id>/<str:reaction_type>/', views.handle_reaction, name='handle_reaction'),

]
