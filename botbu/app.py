import re
from chalice import Chalice
from chalicelib import test_order

app = Chalice(app_name='botbu')

@app.route('/')
def index():
    return {'hell0': 'world'}

@app.route('/sell_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body
    data = {
        'symbol': webhook_message['ticker'],
        'qty' : webhook_message['quantity'],
        'side' : 'sell',
        'kucoin_api_public_key': webhook_message['kucoin_api_public_key'],
        'kucoin_api__secret_key' : webhook_message['kucoin_api__secret_key'],
        'kucoin_api_pass' : webhook_message['kucoin_api_pass']
    }
    order_result, info = test_order.order(data)
    if order_result:
        return {
            'msg': 'I sold the stock',
            'order_id' : info,
            'webhook_msg': webhook_message
        }
    return {
            'msg': 'Failed to sell the stock',
            'error': info,
            'webhook_msg': webhook_message
    }

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body
    data = {
        'symbol': webhook_message['ticker'],
        'qty' : webhook_message['quantity'],
        'side' : 'buy',
        'kucoin_api_public_key': webhook_message['kucoin_api_public_key'],
        'kucoin_api__secret_key' : webhook_message['kucoin_api__secret_key'],
        'kucoin_api_pass' : webhook_message['kucoin_api_pass']
    }
    order_result, info = test_order.order(data)
    if order_result:
        return {
            'msg': 'I bought the stock',
            'order_id' : info,
            'webhook_msg': webhook_message
        }
    return {
            'msg': 'Failed to buy the stock',
            'error': info,
            'webhook_msg': webhook_message
    }

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
