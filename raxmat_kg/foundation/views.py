
from django.shortcuts import render_to_response
from django.contrib import auth


def funds(request):
    return render_to_response('foundations.html', {'username': auth.get_user(request).username})