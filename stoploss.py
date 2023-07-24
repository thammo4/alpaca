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

symbol = "AAPL"
symbol_price = symbol_bars[symbol][0].close
symbol_price

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol=symbol,
                    qty=1,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    type='market',
                    order_class='oto',
                    stop_loss={'stop_price': round(symbol_price * 0.95,2)}
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )