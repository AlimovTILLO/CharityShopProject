# -*-coding: utf-8 -*-

from django.conf.urls import url
from item import views


urlpatterns = [
    url(r'^$', "item.views.index"),
    url(r'^$', "item.views.items"),
    url(r'^items/all/$', "item.views.items"),
    url(r'^items/get/(?P<item_id>\d+)/$', "item.views.item"),
    url(r'^comments_item_id/(\d+)/$', "item.views.item"),
    url(r'^page/(\d+)/$', "item.views.items"),
]

