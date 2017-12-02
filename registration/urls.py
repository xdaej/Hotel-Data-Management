from django.conf.urls import url, include

from registration import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
]