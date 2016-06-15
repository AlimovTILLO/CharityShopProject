from django.conf.urls import url

from foundation import views

urlpatterns = [
    url(r'^funds/$', "foundation.views.funds"),
]
