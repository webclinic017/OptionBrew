from websocket._app import WebSocketApp
import json
import threading
import os
from dotenv import load_dotenv
import requests

class MarketAPI:
  instance = None  # Singleton instance

  @classmethod
  def get_instance(cls):
      if cls.instance is None:
          cls.instance = MarketAPI()
      return cls.instance

  def __init__(self):
      load_dotenv()
      self.api_key = os.getenv('T_ALPACA_API_KEY')
      self.api_secret = os.getenv('T_ALPACA_API_SECRET')
      self.websocket_url = "wss://stream.data.sandbox.alpaca.markets/v2/iex"
      self.connection = None
      self.data = []  # Initialize the data list to store trade data
      self.lock = threading.Lock()
      self.connect_to_stream()

  def on_open(self, ws):
      print("Opened connection")
      auth_data = {"action": "auth", "key": self.api_key, "secret": self.api_secret}
      ws.send(json.dumps(auth_data))

  def on_message(self, ws, message):
      print("Received message:", json.loads(message))
      message = json.loads(message)
      if 'T' in message and message['T'] == 'trade':
          with self.lock:
              # Store each trade update in the data list
              self.data.append({
                  "timestamp": message['timestamp'],
                  "close": message['price']
              })

  def on_error(self, ws, error):
      print("Error:", error)

  def on_close(self, ws, close_status_code, close_msg):
      print("Closed connection:", close_status_code, close_msg)
      with self.lock:
          self.connection = None  # Reset connection on close

  def connect_to_stream(self):
      with self.lock:
          if not self.connection:
              self.connection = WebSocketApp(self.websocket_url,
                                              on_open=self.on_open,
                                              on_message=self.on_message,
                                              on_error=self.on_error,
                                              on_close=self.on_close)
              thread = threading.Thread(target=self.connection.run_forever)
              thread.daemon = True
              thread.start()

  def subscribe_to_stock(self, ticker):
    subscribe_message = {"action": "subscribe", "trades": [ticker]}
    
    if self.connection and self.connection.sock and self.connection.sock.connected:
        self.connection.send(json.dumps(subscribe_message))
    else:
        print("Connection is closed. Reconnecting...")
        self.connect_to_stream()
        # Wait to ensure the connection is established
        threading.Event().wait(1.0)
        # Recheck connection before attempting to send again
        if self.connection and self.connection.sock and self.connection.sock.connected:
            self.connection.send(json.dumps(subscribe_message))
        else:
            print("Failed to reconnect.")

  def fetch_historical_data(self, ticker, start_date, end_date, timeframe='1D'):
    """Fetch historical data for a given ticker within a specified date range using the IEX feed."""
    url = f"https://data.alpaca.markets/v2/stocks/{ticker}/bars"
    headers = {
        'APCA-API-KEY-ID': self.api_key,
        'APCA-API-SECRET-KEY': self.api_secret
    }
    params = {
        'start': start_date,
        'end': end_date,
        'timeframe': timeframe,
        'feed': 'IEX'  # Specify IEX as the data feed
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['bars']
    else:
        raise Exception(f"Failed to fetch historical data: {response.text}")