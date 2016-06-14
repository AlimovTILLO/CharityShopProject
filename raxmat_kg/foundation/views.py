from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from django.contrib import auth
from foundation.models import Foundation


def funds(request):
    all_funds = Foundation.objects.all()
    return render_to_response('foundations.html', {'username': auth.get_user(request).username})