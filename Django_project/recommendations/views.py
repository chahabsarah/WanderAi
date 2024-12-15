# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recommendation
from .forms import RecommendationForm
from voyages.models import Voyage
from preferences.models import Preference, UserProfile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date
from recommendations.recommendation_engine import RecommendationEngine
from django.contrib import messages

# Create
def recommendation_create(request):
    if request.method == "POST":
        form = RecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recommendation-list')
    else:
        form = RecommendationForm()
    return render(request, 'recommendations/add_recommendation.html', {'form': form})

# Read (List)
def recommendation_list(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'recommendations/recommendations_list.html', {'recommendations': recommendations})

# Update
def recommendation_update(request, pk):
    recommendation = get_object_or_404(Recommendation, pk=pk)
    if request.method == "POST":
        form = RecommendationForm(request.POST, instance=recommendation)
        if form.is_valid():
            form.save()
            return redirect('recommendation-list')
    else:
        form = RecommendationForm(instance=recommendation)
    return render(request, 'recommendations/modifier_recommendation.html', {'form': form})

# Delete
def recommendation_delete(request, pk):
    recommendation = get_object_or_404(Recommendation, pk=pk)
    if request.method == "POST":
        recommendation.delete()
        return redirect('recommendation-list')
    return render(request, 'recommendations/recommendation_confirm_delete.html', {'recommendation': recommendation})


def recommendation_detail(request, recommandation_id):
    recommendation = get_object_or_404(Recommendation, id=recommandation_id)

    return render(request, 'recommendations/recommendation_detail.html', {'recommendation': recommendation})

@login_required
def recommendations_for_user(request):
    try:
        print(f"Utilisateur connecté : {request.user}")
        user_profile =request.user
        print(f"Profil utilisateur : {user_profile}")

        user_preferences = Preference.objects.get(user=user_profile)
        print(f"Préférences utilisateur : {user_preferences}")

  
    finally:
        recommended_voyages = RecommendationEngine.get_recommendations(user_preferences)
        if not recommended_voyages:
            messages.info(request, "Aucune recommandation trouvée. Essayez d'ajuster vos préférences.")

        return render(request, 'recommendations/recommendations_list.html', {
            'recommended_voyages': recommended_voyages
        })
