import pandas as pd;
import numpy as np;
import math;
import os;


# keys.py contains API_KEY_ID and SECRET_KEY
from keys import *
from alpaca.trading.client import TradingClient

BASE_URL = "https://paper-api.alpaca.markets";


trading_client = TradingClient(API_KEY_ID, SECRET_KEY, paper=True);


# confirm successful connection
print(trading_client);