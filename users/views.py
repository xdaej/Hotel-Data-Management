from django.shortcuts import render


def login(request):
    return render(request,'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')