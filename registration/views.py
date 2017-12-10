from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from .forms import UserForm

def registration(request):
    return render(request, 'registration/hell_world.html')

def success(request):
    return render(request, 'registration/registration_success.html')


def register(request):
    if request.method == 'POST':
        #form = UserForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('registration/registration_success.html')
    else:
        #form = UserForm()
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form':form})