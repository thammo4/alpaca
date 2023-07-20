from config import *

from alpaca.trading.client import TradingClient;
from alpaca.trading.requests import MarketOrderRequest;
from alpaca.trading.enums import OrderSide, TimeInForce;


#
# From config file
#
# Connect to trading client paper account
# trading_client = TradingClient(API_KEY_ID, SECRET_KEY, paper=True);
#

# print(trading_client);

#
# Convenience function for ez market buy orders
# Orders are good for the entire trading day
#

def mrkt_buy (symbol='', qty=0):
    if not isinstance(symbol, str):
        return 'wtf malformed symbol';
    if not (isinstance(qty,float) or isinstance(qty, int)):
        return 'wtf quantity';

    mrkt_buy_data   = MarketOrderRequest(symbol=symbol, qty=qty, side=OrderSide.BUY, time_in_force=TimeInForce.DAY);
    mrkt_buy        = trading_client.submit_order(order_data=mrkt_buy_data);

    print('looks good to me!');