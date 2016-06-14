import time

from item.models import Item, request
import jwt
from sellerinfo import SELLER_ID
from sellerinfo import SELLER_SECRET

app = Item(__name__)


@app.route('/response', methods=['POST'])
def response():
    data = request.data
    jwt_info = jwt.decode(data, SELLER_SECRET)
    assert jwt_info['iss'] == SELLER_ID
    assert jwt_info['exp'] >= time.time()
    request_info = jwt_info['request']
    response_info = jwt_info['response']
    print request_info['sellerData']
    print response_info['orderId']
    return response_info['orderId'], 200
