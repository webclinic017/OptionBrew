# Market Data Utility Classes to fetch and display ticker data...
from alpaca.data.historical import CryptoHistoricalDataClient, StockHistoricalDataClient, OptionHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream
from datetime import datetime   
import os
from dotenv import load_dotenv

class MarketAPI(): 
  def __init__(self):
    load_dotenv()
    self.api_key = os.getenv('T_ALPACA_API_KEY')
    self.api_secret = os.getenv('T_ALPACA_API_SECRET')
    self.base_url = "https://paper-api.alpaca.markets/v2"
    # Full WebSocket URL : wss://stream.data.sandbox.alpaca.markets/{version}/{feed}
    self.websocket_url_stocks = "wss://stream.data.sandbox.alpaca.markets/v2/{feed}"
    cryptoClient = CryptoHistoricalDataClient() # No keys needed for this client
    stock_client = StockHistoricalDataClient(self.api_key,  self.api_secret)
    option_client = OptionHistoricalDataClient(self.api_key,  self.api_secret)

  def display_stream(self):
    pass

  def stock_websocket(self, ticker):
    sds = StockDataStream(self.api_key, self.api_secret, True, IEX)
    sds.subscribe_bar(self.display_stream, "AAPL")
    sds.run()

