import alpaca_trade_api as tradeapi # old

#  new stuff
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime


from config import *

# API_KEY_ID and SECRET_KEY


client = StockHistoricalDataClient(API_KEY_ID, SECRET_KEY);

request_params = StockBarsRequest(
                        symbol_or_symbols=["AAPL", "SPY"],
                        timeframe=TimeFrame.Day,
                        start=datetime.strptime("2023-07-21", '%Y-%m-%d')
);

bars = client.get_stock_bars(request_params)


symbol = bars['AAPL'][0].symbol;
last_close_price = bars['AAPL'][0].close;

# bars.df.head(50)

# api = tradeapi.REST(API_KEY_ID, SECRET_KEY);

# # symbol = 'AAPL'
# # symbol_bars = api.get_barset(symbol, 'minute', 1).df.iloc[0]
# # last_close_price = symbol_bars[symbol]['close']

# # We could buy a position and add a stop-loss and a take-profit of 5 %
# api.submit_order(
#     symbol=symbol,
#     qty=1,
#     side='buy',
#     type='market',
#     time_in_force='gtc',
#     order_class='bracket',
#     stop_loss={'stop_price': last_close_price * 0.95,
#                'limit_price':  last_close_price * 0.94},
#     take_profit={'limit_price': last_close_price * 1.05}
# )

# # We could buy a position and just add a stop loss of 5 % (OTO Orders)
# api.submit_order(
#     symbol=symbol,
#     qty=1,
#     side='buy',
#     type='market',
#     time_in_force='gtc',
#     order_class='oto',
#     stop_loss={'stop_price': last_close_price * 0.95}
# )

# # We could split it to 2 orders. first buy a stock,
# # and then add the stop/profit prices (OCO Orders)
# api.submit_order(symbol, 1, 'buy', 'limit', 'day', last_close_price)

# # wait for it to buy position and then
# api.submit_order(
#     symbol=symbol,
#     qty=1,
#     side='sell',
#     type='limit',
#     time_in_force='gtc',
#     order_class='oco',
#     stop_loss={'stop_price': last_close_price * 0.95},
#     take_profit={'limit_price': last_close_price * 1.05}
# )