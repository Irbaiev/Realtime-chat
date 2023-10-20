from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rooms.models import Rooms, Message


@login_required
def rooms(request):
    rooms = Rooms.objects.all()

    return render(request, "rooms.html", {"rooms": rooms})


@login_required
def room(request, slug):
    room = Rooms.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, "room.html", {"room": room, "messages": messages})
