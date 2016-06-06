from django.shortcuts import render_to_response
from cart import Cart
from item.models import Item


def add_to_cart(request, product_id, quantity):
    product = Item.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)


def remove_from_cart(request, product_id):
    product = Item.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)


def get_cart(request):
    return render_to_response('cart.html', dict(cart=Cart(request)))
