from django.shortcuts import render, redirect, get_object_or_404
from .models import Preference, UserProfile
from .forms import PreferenceForm
from django.contrib.auth.decorators import login_required

@login_required  # Assurez-vous que l'utilisateur est connecté
def preference_create(request):
    if request.method == "POST":
        form = PreferenceForm(request.POST)
        if form.is_valid():
            # Vérifier si un UserProfile existe pour l'utilisateur connecté
            user_profile =request.user
            
            # Sauvegarder la préférence avec l'utilisateur connecté
            preference = form.save(commit=False)
            preference.user = user_profile  # Assigner l'instance UserProfile
            preference.save()  # Sauvegarder l'objet Preference
            
            return redirect('preference-list')  # Rediriger vers la liste des préférences
    else:
        form = PreferenceForm()  # Préparer le formulaire
    return render(request, 'preferences/add_preference.html', {'form': form})

# Read (List)
def preference_list(request):
    preferences = Preference.objects.all()
    return render(request, 'preferences/preferences_list.html', {'preferences': preferences})

# Update
def preference_update(request, pk):
    preference = get_object_or_404(Preference, pk=pk)
    if request.method == "POST":
        form = PreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            return redirect('preference-list')
    else:
        form = PreferenceForm(instance=preference)
    return render(request, 'preferences/modifier_preference.html', {'form': form})

# Delete
def preference_delete(request, pk):
    preference = get_object_or_404(Preference, pk=pk)
    if request.method == "POST":
        preference.delete()
        return redirect('preference-list')
    return render(request, 'preferences/preference_confirm_delete.html', {'preference': preference})
