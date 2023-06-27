from config import *

from alpaca.broker.client import BrokerClient;
from alpaca.broker.requests import ListAccountsRequest;
from alpaca.broker.enums import AccountEntities;

from alpaca.trading.client import TradingClient

# instantiate tradingclient object
trading_client = TradingClient(API_KEY_ID, SECRET_KEY, paper=True);


#
# Testing out some methods in the alapca package
#

# Get market clock data
#
# >>> trade_clock
# {   'is_open': True,
#     'next_close': datetime.datetime(2023, 6, 27, 16, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))),
#     'next_open': datetime.datetime(2023, 6, 28, 9, 30, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))),
#     'timestamp': datetime.datetime(2023, 6, 27, 12, 38, 34, 401116, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))}
trading_clock = trading_client.get_clock();





# Fetch data about watchlists created
#
# >>> trading_client.get_watchlists()
# [{   'account_id': UUID('ee77eb9a-11e8-4a08-a999-81660f3f4eed'),
#     'assets': None,
#     'created_at': datetime.datetime(2021, 5, 28, 6, 20, 34, 262800, tzinfo=datetime.timezone.utc),
#     'id': UUID('2d43533c-4cf0-469d-9efc-d39758f05de8'),
#     'name': 'Primary Watchlist',
#     'updated_at': datetime.datetime(2021, 5, 28, 6, 20, 34, 262800, tzinfo=datetime.timezone.utc)}]
trading_watchlists = trading_client.get_watchlists();












