from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rooms.models import Rooms

@login_required
def rooms(request):
    rooms = Rooms.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):

    room = Rooms.objects.get(slug=slug)

    return render(request, 'room.html', {'room': room})
