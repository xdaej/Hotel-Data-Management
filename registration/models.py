from django.db import models
from django import forms

class User(forms.ModelForm):
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    #phone_number = models.IntegerField(max_length=250)
    #address = models.CharField(max_length=250)
    password = models.CharField(max_length=250)



