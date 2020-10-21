from django.shortcuts import render

from .models import Squirrel


def main(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }

    return render(request, 'sightings/main.html', context)
