from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rooms.models import Rooms

@login_required
def rooms(request):
    rooms = Rooms.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})
