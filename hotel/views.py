from django.shortcuts import render

def hello_word(request):
    return render(request,'layout.html')

def login(request):
    return render(request, 'registration/../templates/login.html')