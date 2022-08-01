from django.shortcuts import render
from .models import Car, Home, About
# Create your views here.

def home(request):
    homes = Home.objects.all()
    return render(request, 'home.html', {'homes':homes})


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars':cars})

def about(request):
    abouts = About.objects.all()
    return render(request, 'about.html', {'abouts':abouts})
