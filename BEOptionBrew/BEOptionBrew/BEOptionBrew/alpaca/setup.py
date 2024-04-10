import os 
import requests

ALPACA_API_KEY = os.getenv('B_ALPACA_API_KEY')
ALPACA_API_SECRET = os.getenv('B_ALPACA_API_SECRET')
ALPACA_PAPER_URL = "https://broker-api.sandbox.alpaca.markets"

headers = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_API_SECRET,
}

# Format the data according to Alpaca's required format
data = {
    # Populate this dictionary with the user data formatted as required by Alpaca
}

response = requests.post(f"{ALPACA_PAPER_URL}/v1/accounts", json=data, headers=headers)

if response.status_code in (200, 201):
    print("Account creation successful")
    account_info = response.json()
    print(account_info)
else:
    print("Account creation failed", response.text)