from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),               # General home page
    path('admin/', admin.site.urls),              # Django admin
    path('', include('theme_soft_design.urls')),  # Front-end interface
    path('back/', include('admin_soft.urls')),    # Back-end interface
    path('experiences/', include('experiences.urls')),
    path('avis/', include('Avis.urls')),  
    path('voyage/', include('voyages.urls')),  
    path('preferences/', include('preferences.urls')),
    path('recommendations/', include('recommendations.urls')),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('destinations/', include('destination.urls')), 
    path('itineraires/', include('itineraire.urls'))  ,
    path('reservations/', include('reservation.urls'))  ,

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
