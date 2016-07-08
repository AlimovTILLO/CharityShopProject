from django.conf.urls import url

from item.views import funds

urlpatterns = [
    url(r'^funds/$', funds, name="funds"),
]
