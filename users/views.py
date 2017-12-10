from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)



def login(request):
    return render(request,'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')