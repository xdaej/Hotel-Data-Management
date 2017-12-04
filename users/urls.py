from django.conf.urls import url, include

from users import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^', views.login, name="login"),
    url('^', include('django.contrib.auth.urls')),
]