from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse

from .cart import Cart
from django.shortcuts import render_to_response
from item.models import Item


def add_to_cart(request, item_id, quantity):
    item = Item.objects.get(id=item_id)
    cart = Cart(request)
    cart.add(item, item.item_price, quantity)
    return JsonResponse({'status': 'ok'})


def remove_from_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    cart = Cart(request)
    cart.remove(item)
    return JsonResponse({'status': 'ok'})


def remove_all(request):
    Cart(request).remove_all()
    return JsonResponse({'status': 'ok'})


def show(request):
    return render_to_response('cart.html', dict(cart=Cart(request)))
