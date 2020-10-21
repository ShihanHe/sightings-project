from django.shortcuts import render
from .models import Squirrel

from django.http import HttpResponse



def list_of_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/list.html', context)

def update_squirrel(request):

    
    return render(request, 'sightings/update.html', context)

def create_squirrel(request):

    
    return render(request, 'sightings/create.html', context)

def stats(request):
    

    return render(request, 'sightings/stats.html',context)
