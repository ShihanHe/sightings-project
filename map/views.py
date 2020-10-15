from django.shortcuts import render
from sightings.models import Squirrel

def map(request):
    
    squirrels = Squirrel.objects.all()[:100]

    context = { 'squirrels' : squirrels, }

    return render(request,'map/map.html',context)
