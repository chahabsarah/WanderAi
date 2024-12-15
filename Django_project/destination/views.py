# destination/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination  # Import your Destination model

# List View
def destination_list(request):
    destinations = Destination.objects.all()  # Get all destinations
    return render(request, 'destination/destination_list.html', {'destinations': destinations})

def destination_create(request):
    if request.method == 'POST':
        nom = request.POST['nom']  # Make sure to use the correct field name
        description = request.POST['description']
        image = request.FILES.get('image')  # Handle the uploaded file
        
        # Create a new destination
        Destination.objects.create(nom=nom, description=description, image=image)  
        
        return redirect('destination:list')  # Use the correct namespace and name
    return render(request, 'destination/destination_create.html')



# Update View
def destination_update(request, pk):  # Change 'id' to 'pk'
    destination = get_object_or_404(Destination, pk=pk)  # Use 'pk'
    if request.method == 'POST':
        destination.nom = request.POST['name']
        destination.description = request.POST['description']  # Update description
        if 'image' in request.FILES:
            destination.image = request.FILES['image']  # Update image if provided
        destination.save()  # Save the updated destination
        return redirect('destination:list')  # Redirect to destination list
    return render(request, 'destination/destination_update.html', {'destination': destination})

# Delete View
def destination_delete(request, pk):  # Change 'id' to 'pk'
    destination = get_object_or_404(Destination, pk=pk)  # Use 'pk'
    if request.method == 'POST':
        destination.delete()  # Delete the destination
        return redirect('destination:list')  # Redirect to destination list
    return render(request, 'destination/destination_delete.html', {'destination': destination})