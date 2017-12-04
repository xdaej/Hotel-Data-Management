from django.conf.urls import url, include

from registration import views

urlpatterns = [
    url(r'^', views.registration, name="registration"),
]