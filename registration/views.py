from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

def registration(request):
    return render(request, 'registration/registration.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/success.html')
    else:
        form = UserForm()
    return render(request, 'registration/registration.html', {'form':form})