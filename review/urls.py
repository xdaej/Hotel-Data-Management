from django.conf.urls import url, include

from review import views

urlpatterns = [
    url(r'^', views.review, name="review"),
]