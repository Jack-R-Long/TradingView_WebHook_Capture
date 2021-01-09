import kucoin.client as kuclinet
from api_creds import *

order_ids=[]

def order(side, quantity, symbol):
    client = kuclinet.Client(KU_API_PUBLIC, KU_API_SECRET, KU_PASSPHRASE)
    try:
        print('\nSending order!')
        order = client.create_market_order(symbol, side, quantity)
        print(order)
        order_ids.append(order)
    except Exception as e:
        print('Failed to place order')
        print(e.__cause__)
        return (False, e)
    return (True, order)

if __name__=='__main__':
    order('buy', .01, 'ETH-USDT' )
