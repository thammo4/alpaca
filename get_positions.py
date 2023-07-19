from config import *
from alpaca.trading.client import TradingClient;

trading_client = TradingClient(API_KEY_ID, SECRET_KEY, paper=True);

#
# Convenience function to get current positions in ez-to-use dataframe
#

def get_positions ():
	df_positions = pd.DataFrame();
	positions = trading_client.get_all_positions();
	for x in positions:
		df_x = pd.json_normalize(dict(x));
		df_positions = pd.concat([df_positions, df_x], ignore_index=True);
	return df_positions;


current_positions = get_positions();
print("\nCURRENT POSITIONS");
print(current_positions);