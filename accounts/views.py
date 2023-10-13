from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import RegisterUserForm

def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
        
    else:
        form = RegisterUserForm

    return render(request, 'registration/register.html', {'form': form})