from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Squirrel
from .forms import SquirrelForm, UpdatingForm
from django.http import HttpResponse



def list_of_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/list.html', context)

def update(request, Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = UpdatingForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = UpdatingForm(instance=squirrel)
    
    context ={
        'form':form,
        'sqid':Unique_Squirrel_ID,
    }

    return render(request, 'sightings/update.html', context)


def create_squirrel(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")
    else:
        form = SquirrelForm()
    context = {
            'form':form,
    }
    return render(request, 'sightings/add.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    a = len(squirrels)
    b = squirrels.aggregate(min_latitude=Min('Latitude'),max_latitude=Max('Latitude'),average_latitude=Avg('Latitude'))
    c = squirrels.aggregate(min_latitude=Min('Longitude'),max_latitude=Max('Longitude'),average_latitude=Avg('Longitude'))
    d = list(squirrels.values_list('Shift').annotate(Count('Shift')))
    e = list(squirrels.values_list('Age').annotate(Count('Age')))
    f = list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))

    contex = {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "f": f,
    }

    return render(request, 'sightings/stats.html',context)
