# -*-coding: utf-8 -*-

from django.conf.urls import url

from item.views import CategoryProduct

urlpatterns = {
    url(r'^$', "item.views.index"),
    url(r'^$', "item.views.items"),
    url(r'^category/(?P<pk>\d+)/$', CategoryProduct.as_view(), name="category-id"),
    url(r'^items/all/$', "item.views.items"),
    url(r'^items/get/(?P<item_id>\d+)/$', "item.views.item"),
    url(r'^items/addcomment/(?P<item_id>\d+)/$', "item.views.addcomment"),
    url(r'^comments_item_id/(\d+)/$', "item.views.item"),
    url(r'^page/(\d+)/$', "item.views.items"),

}
