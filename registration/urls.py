from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from registration import views

urlpatterns = [
    url(r'^register/$', views.registration, name='register'),
    url(r'^', views.register, name="registration"),
    url(r'^success/$', views.success, name='success'),
]