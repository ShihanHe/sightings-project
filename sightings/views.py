from django.shortcuts import render
from .models import Squirrel



def list_of_squirrel(request):


    return render(request, 'sightings/lists.html', context)

def update_squirrel(request):

    
    return render(request, 'sightings/update.html', context)

def create_squirrel(request):

    
    return render(request, 'sightings/create.html', context)

def stats(request):
    

    return render(request, 'sightings/stats.html',context)
