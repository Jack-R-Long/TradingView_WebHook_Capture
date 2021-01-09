import kucoin.client as kuclinet
from api_creds import *


client = kuclinet.Client(KU_API_PUBLIC, KU_API_SECRET, KU_PASSPHRASE)
order_ids=[]

def order(side, quantity, symbol):
    try:
        print('\nSending order!')
        order = client.create_market_order(symbol, side, quantity)
        print(order)
        order_ids.append(order)
    except Exception as e:
        print('Failed to place order')
        print(e.__cause__)
        return False
    return True

if __name__=='__main__':
    order('buy', .01, 'ETH-USDT' )
