from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^foundations/$', "foundation.views.foundations"),
]
