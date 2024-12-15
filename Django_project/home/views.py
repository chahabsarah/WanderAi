from django.shortcuts import render

def front_home(request):
    return render(request, 'pages/accueil.html')  # Ensure the template path is correct

def back_home(request):
    return render(request, 'pages/accueil.html')  # Ensure the template path is correct
