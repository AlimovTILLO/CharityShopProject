# coding=utf-8
import time

from cart import cart
from cart.models import render_template, Cart

import jwt
from sellerinfo import SELLER_ID
from sellerinfo import SELLER_SECRET

app = Cart(__name__)


@app.route('/')
def index():
    product_info = [
        {'name': "A Virtual chocolate cake to fill your virtual tummy ",
         'price': "25.00"
         }]

    request_info = {
        'currencyCode': 'KGS',
        'sellerData': u"Номер транзакции",
        'totalSum': cart.summary,
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
    return render_template('mobilnik.html', jwt=token, key=SELLER_ID)
