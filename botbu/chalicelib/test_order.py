import kucoin.client as kuclinet
from .api_creds import *

order_ids=[]

def order(data):
    # client = kuclinet.Client(KU_API_PUBLIC, KU_API_SECRET, KU_PASSPHRASE)
    client = kuclinet.Client(data['kucoin_api_public_key'], data['kucoin_api__secret_key'], data['kucoin_api_pass'])
    fixed_symbol = eth_tick_fix(data['symbol'])
    try:
        print('\nSending order!')
        order = client.create_market_order(fixed_symbol, data['side'], data['qty'])
        print(order)
        order_ids.append(order)
    except Exception as e:
        print('Failed to place order')
        print(e.__cause__)
        return (False, str(e.__cause__))
    return (True, order)

def eth_tick_fix(eth_ticker):
    if 'ETH' in eth_ticker:
        return 'ETH-USDT'
    return 'WRONG'

if __name__=='__main__':
    order('buy', .01, 'ETH-USDT' )
