#-*-coding: utf-8 -*-
from django.conf.urls import url, patterns
from .views import logout,login,register
urlpatterns = [
    url(r'^login', login),
    url(r'^logout', login),
  	url(r'^register', register),
]