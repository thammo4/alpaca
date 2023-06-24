from config import *

# Create account object
account = trading_client.get_account();


# Iterate over JSON and print each key:value pair in a newline
for key,val in account:
	print(f"\"{key}\":{val}");