from django.conf.urls import url, include

from reservation import views

urlpatterns = [
    url(r'^', views.reservation, name="reservation"),
]