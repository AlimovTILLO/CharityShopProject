# coding=utf-8
import time

from django.shortcuts import render

from cart import cart
from cart.models import Cart, Item

import jwt
from sellerinfo import SELLER_ID
from sellerinfo import SELLER_SECRET

app = Cart(__name__)


def index(request):
    product_info = [
        {'name': Item.product,
         'price': Item.total_price
         }]

    request_info = {
        'currencyCode': 'KGS',
        'sellerData': cart,
        'totalSum': cart.Cart.summary,
        'description': u"Информация о заказе",
        'products': product_info
    }
    curr_time = int(time.time())
    exp_time = curr_time + 3600

    jwt_info = {
        'iss': SELLER_ID,
        'aud': 'mobilnik.kg',
        'typ': 'acquiring.mobilnik.kg/api/v1',
        'iat': curr_time,
        'exp': exp_time,
        'request': request_info
    }
    token = jwt.encode(jwt_info, SELLER_SECRET)
    return render('mobilnik.html', jwt=token, key=SELLER_ID)
