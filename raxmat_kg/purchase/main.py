# coding=utf-8
import time

from django.contrib import auth
from django.shortcuts import render_to_response

from cart.models import Cart

import jwt
from sellerinfo import SELLER_ID
from sellerinfo import SELLER_SECRET

app = Cart(__name__)


def index(request):
    product_info = [
        {'name': 'Samsung',  # ==>
         'price': 25  # ==>
         }]

    request_info = {
        'currencyCode': 'KGS',
        'sellerData': 1,  # ==>
        'totalSum': 25,  # ==>
        'description': u"Информация о заказе",
        'products': product_info,
        'test': True  # ==>
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
    return render_to_response('order_list.html',
                              {'jwt': token, 'key': SELLER_ID, 'username': auth.get_user(request).username})
