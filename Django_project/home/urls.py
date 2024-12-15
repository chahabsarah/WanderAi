from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/login/', views.front_home, name='front_home'),
    path('back/', views.back_home, name='back_home'),
    path('', RedirectView.as_view(url='/back/accounts/login/', permanent=False))
]
