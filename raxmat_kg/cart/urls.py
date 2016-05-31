
from django.conf.urls import url

urlpatterns = [
    url(r'^add/$', "cart.views.add_to_cart"),
    url(r'^remove/$', "cart.views.remove_from_cart"),
    url(r'^show/$', "cart.views.get_cart"),
]


