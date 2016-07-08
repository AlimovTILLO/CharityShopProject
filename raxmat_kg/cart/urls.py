from django.conf.urls import url

from purchase.main import index
from purchase.views import address_select, order_detail

from .views import add_to_cart, remove_from_cart, show, remove_all

urlpatterns = [
    url(r'^add/(?P<item_id>\d+)/(?P<quantity>\d+)/$', add_to_cart, name='add'),
    url(r'^remove/(?P<item_id>\d+)/$', remove_from_cart, name='remove'),
    url(r'^remove_all/$', remove_all, name='remove_all'),
    url(r'^show/$', show, name='show'),
    url(r'^purchase/step_one/$', address_select, name='address_select'),
    url(r'^purchase/step_two/$', order_detail, name='order_detail'),
    url(r'^purchase/step_three/$', index, name='order_list'),
]
