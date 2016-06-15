# -*-coding: utf-8 -*-
from django.conf.urls import url, patterns
from .views import logout, login, register, settings

urlpatterns = [
    url(r'^login', login),
    url(r'^logout', logout),
    url(r'^register', register),
    url(r'^settings/$', settings, {
        'templates': 'settings.html'
    }, 'settings'),
]
