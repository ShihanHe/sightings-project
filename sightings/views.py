from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Squirrel
from .forms import SquirrelForm
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
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm(instance=squirrel)
    
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
    

    return render(request, 'sightings/stats.html',context)
