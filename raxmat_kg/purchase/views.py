from django.contrib import auth
from django.shortcuts import render_to_response

# Create your views here.
from cart.models import Item


def purchase(request):
    Item.cart
    Item.total_price
    Item.content_type
    Item.unit_price
    Item.object_id
    Item.quantity
    return render_to_response('purchase.html', {'username': auth.get_user(request).username})
