from django.contrib import admin
from preferences.models import UserProfile, Preference
from experiences.models import Experience
from Avis.models import Avis
from recommendations.models import Recommendation
from voyages.models import Voyage
from reservation.models import Reservation


admin.site.register(Reservation)

admin.site.register(UserProfile)
admin.site.register(Preference)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('user', 'note', 'commentaire')  # Liste des colonnes à afficher
    search_fields = ('user', 'note', 'commentaire')  # Champs sur lesquels faire des recherches

class VoyageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'destination', 'date_depart', 'date_retour', 'prix')
    search_fields = ('nom', 'destination', 'date_depart', 'date_retour', 'prix')
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience_name', 'date_recommended')
    search_fields = ('experience_name', 'user__name')
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category')
    search_fields = ('title','price', 'category')
admin.site.register(Avis, AvisAdmin)  # Enregistre le modèle Avis avec la personnalisation
admin.site.register(Recommendation, RecommendationAdmin) 
admin.site.register(Voyage, VoyageAdmin)  # Enregistre le modèle Avis avec la personnalisation
admin.site.register(Experience, ExperienceAdmin) 