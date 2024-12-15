# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Experience
from .forms import ExperienceForm
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from experiences.models import UserReaction
@login_required

def handle_reaction(request, experience_id, reaction_type):
    try:
        # Get the experience object
        experience = Experience.objects.get(id=experience_id)
        
        # Get or create a UserReaction for the user and the experience
        user_reaction, created = UserReaction.objects.get_or_create(
            user=request.user, experience=experience
        )
        
        # Update the reaction type
        user_reaction.reaction = reaction_type
        user_reaction.save()
        
        # Count the number of "like" reactions
        like_count = UserReaction.objects.filter(experience=experience, reaction='like').count()

        return JsonResponse({'like_count': like_count})

    except Experience.DoesNotExist:
        return JsonResponse({'error': 'Experience not found'}, status=404)
def experience_create(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST, request.FILES)  # Utilisez request.FILES pour les fichiers
        if form.is_valid():
            form.save()
            return redirect('experience-list')
    else:
        form = ExperienceForm()
    return render(request, 'experiences/add_experience.html', {'form': form})
# Read (List)
def experience_list(request):
    experiences = Experience.objects.all()

    # For each experience, calculate the like count
    for experience in experiences:
        experience.like_count = experience.userreaction_set.filter(reaction='like').count()

    return render(request, 'experiences/experience_list.html', {'experiences': experiences})
# Update
def experience_update(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experience-list')  # Redirige après la mise à jour
    else:
        form = ExperienceForm(instance=experience)
    
    return render(request, 'experiences/modifier_experience.html', {'form': form})
def experience_delete(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        experience.delete()
        return redirect('experience-list')
    return render(request, 'experiences/experience_confirm_delete.html', {'experience': experience})
