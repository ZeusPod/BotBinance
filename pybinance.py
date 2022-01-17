import os
from dotenv import load_dotenv
import keyboard
from binance.client import Client
from binance.streams import BinanceSocketManager

from twisted.internet import reactor

load_dotenv()
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')



client = Client(api_key, api_secret)

prices = client.get_all_tickers()



def get_symbols():
    for price in prices:
        list_prices = price['symbol']
        

def get_price(command):
    command = command.upper()
    symbol = (f'{command}USDT')
    price = client.get_symbol_ticker(symbol = symbol)
    return (price)
    

mi_precio = get_symbols()