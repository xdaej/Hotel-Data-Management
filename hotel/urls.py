"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from registration import urls as registration_urls
from reservation import urls as reservation_urls
from users import urls as users_urls
from review import urls as review_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', include(registration_urls)),
    url(r'^reservation/', include(reservation_urls)),
    url(r'^users/', include(users_urls)),
    url(r'^review/', include(review_urls)),
    url(r'^$', TemplateView.as_view(template_name='layout.html'), name='home'),
    url(r'aboutus/', TemplateView.as_view(template_name='aboutus.html'), name='aboutus')
]
