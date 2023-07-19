from config import *

from alpaca.broker.client import BrokerClient;
from alpaca.broker.requests import ListAccountsRequest;
from alpaca.broker.enums import AccountEntities;

from alpaca.trading.client import TradingClient;

trading_client = TradingClient(API_KEY_ID, SECRET_KEY, paper=True);





#
# Fetch all current open positions and convert them into a pandas DataFrame
#

positions = trading_client.get_all_positions();

df_positions = pd.DataFrame();
for x in positions:
	dict_x 			= dict(x);
	df_x 			= pd.json_normalize(dict_x);
	df_positions 	= pd.concat([df_positions, df_x], ignore_index=True);

print("CURRENT POSITIONS\n");
print(df_positions);

print("COLUMN NAMES\n");
print(df_positions.columns);



#
# Fetch current account information and store as an easy-read dataframe
#

df_account = pd.json_normalize(dict(trading_client.get_account())).T;

print("\nACCOUNT INFORMATION");
print(df_account);


# # This gets screwed up because each element of the resulting dataframe contains a (key,value) pair
# positions = pd.DataFrame(trading_client.get_all_positions());
# print(positions); print("\n");


# # Attempt to convert one element of the alpaca.trading.models.Position object into dataframe
# # pos1 = positions[0];
# # print(pos1); print("\n");

# # dict1 = dict(pos1);
# # print(dict1); print("\n");

# # df1 = pd.json_normalize(dict1);
# # print(df1); print("\n");

# pos1 	= trading_client.get_all_positions()[0];
# dict1 	= dict(pos1);
# df1 	= pd.json_normalize(dict1);

# pos2 	= trading_client.get_all_positions()[1];
# dict2 	= dict(pos2);
# df2 	= pd.json_normalize(dict2);


# print("DF1:\n"); print(df1); print("\n");

# print("DF2:\n"); print(df2); print("\n");




# # RESULTING DATAFRAME COLUMNS
# # >>> df1.columns
# # Index(['asset_id', 'symbol', 'exchange', 'asset_class', 'asset_marginable',
# #        'avg_entry_price', 'qty', 'side', 'market_value', 'cost_basis',
# #        'unrealized_pl', 'unrealized_plpc', 'unrealized_intraday_pl',
# #        'unrealized_intraday_plpc', 'current_price', 'lastday_price',
# #        'change_today', 'swap_rate', 'avg_entry_swap_rate', 'usd',
# #        'qty_available'],
# #       dtype='object')