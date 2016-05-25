# -*-coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.index),
    url(r'^items/all/$', views.items, name='items'),
    url(r'^items/get/(?P<item_id>\d+)/$', views.item, name='item'),
    url(r'^comments_item_id/(\d+)/$', views.item, name='item'),
    url(r'^page/(\d+)/$', views.items, name='items'),
)
