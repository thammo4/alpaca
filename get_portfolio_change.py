from config import *

from alpaca.trading.client import TradingClient;
from alpaca.trading.requests import GetAssetsRequest;


#
# Convenience function to get change in portfolio value for yesterday->today
#

def get_portfolio_change ():
  trading_client = TradingClient(API_KEY_ID, SECRET_KEY, paper=True);
  acct = trading_client.get_account();
  acct_bal_change = round(float(acct.equity) - float(acct.last_equity), 2);
  return acct_bal_change;

# Try it out
acct_change = get_portfolio_change();
print(acct_change);