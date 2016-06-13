from django.conf.urls import url
from .views import add_to_cart, remove_from_cart, show, remove_all

urlpatterns = [
    url(r'^add/(?P<item_id>\d+)/(?P<quantity>\d+)/$', add_to_cart, name='add'),
    url(r'^remove/(?P<item_id>\d+)/$', remove_from_cart, name='remove'),
    url(r'^remove_all/$', remove_all, name='remove_all'),
    url(r'^show/$', show, name='show'),
]
