# urls.py
from django.urls import path
from .views import recommendation_create, recommendation_list, recommendation_update, recommendation_delete
from recommendations.views import recommendation_detail
from recommendations import views

urlpatterns = [
    path('', recommendation_list, name='recommendation-list'),
    path('create/', recommendation_create, name='recommendation-create'),
    path('update/<int:pk>/', recommendation_update, name='recommendation-update'),
    path('delete/<int:pk>/', recommendation_delete, name='recommendation-delete'),
    path('<int:recommandation_id>/detail/', recommendation_detail, name='recommendation-detail'),
    path('recommendations/', views.recommendations_for_user, name='recommendations_for_user'),

]
