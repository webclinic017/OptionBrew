# Broker Utility Classes to sign users up, execute positions, and more... 
import os
import requests
import random
import datetime
import base64
from .models import User



class AlpacaAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('B_ALPACA_API_KEY')
        self.api_secret = os.getenv('B_ALPACA_API_SECRET')
        self.base_url = "https://broker-api.sandbox.alpaca.markets"
        encoded_credentials = base64.b64encode(f"{self.api_key}:{self.api_secret}".encode()).decode()
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {encoded_credentials}"
        }
        
    def _send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data, headers=self.headers)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            # Log detailed error information
            print(f"Failed API call. Status Code: {response.status_code}. Response: {response.text}")
            raise Exception(f"API request failed: {response.status_code} {response.text}")


class Users(AlpacaAPI):
    def registerUser(self, first_name, last_name, email, phone_number):
        user_data = {"first_name": first_name, "last_name": last_name, "email": email, "phone_number": phone_number}
        endpoint = "/v1/accounts"
        alpaca_formatted_data = self._transform_data_to_alpaca_format(user_data)
        
        response = self._send_request('post', endpoint, data=alpaca_formatted_data)
        
        if response and 'id' in response:
            # Assuming `user` is the instance of the User model you are working with
            user = User.objects.get(phone_number=phone_number)
            user.alpaca_account_id = response['id']
            user.save()
            return response['id']  # Return the Alpaca account ID
        else:
            raise Exception("Failed to create Alpaca account or retrieve account ID.")


    def _transform_data_to_alpaca_format(self, user_data):
        dummy_ssn = self._generate_dummy_ssn()
        dummy_date = datetime.datetime.now().isoformat() + 'Z'  # ISO 8601 format
        dummy_phone_number = "+1" + "".join([str(random.randint(0, 9)) for _ in range(10)])
        alpaca_payload = {
            "contact": {
                "email_address": user_data["email"],
                "phone_number": user_data['phone_number'],
                "street_address": ["123 Fake Street"],
                "unit": "string",
                "city": "Faketown",
                "state": "CA",
                "postal_code": "90210"
            },
            "identity": {
                "tax_id_type": "USA_SSN",
                "given_name": user_data["first_name"],
                "family_name": user_data["last_name"],
                "date_of_birth": "1990-01-01",
                "tax_id": dummy_ssn,
                "country_of_citizenship": "USA",
                "country_of_birth": "USA",
                "country_of_tax_residence": "USA",
                "funding_source": ["employment_income"]
            },
            "disclosures": {
                "is_control_person": False,
                "is_affiliated_exchange_or_finra": False,
                "is_politically_exposed": False,
                "immediate_family_exposed": False
            },
            "trusted_contact": {
                "given_name": "Jane",
                "family_name": "Doe",
                "email_address": "jane.doe@example.com"
            },
            "agreements": [
                {
                    "agreement": "customer_agreement",
                    "signed_at": dummy_date,
                    "ip_address": "192.0.2.1"
                }
            ],
            "documents": [
                {
                    "document_type": "identity_verification",
                    "document_sub_type": "passport",
                    "content": "/9j/Cg==",
                    "mime_type": "image/jpeg"
                }
            ],
            "enabled_assets": ["us_equity"]
        }
        return alpaca_payload


    def _generate_dummy_ssn(self):
        area = random.randint(100, 665)
        group = random.randint(1, 99)
        serial = random.randint(1, 9999)
        return f"{area:03d}-{group:02d}-{serial:04d}"

class Trades(AlpacaAPI):
    def open_position(self, symbol, qty, side, type='market', time_in_force='gtc'):
        alpaca_account_id = 0
        endpoint = f'/v1/trading/accounts/{alpaca_account_id}/orders'
        data = {
            "symbol": symbol,
            "qty": qty,
            "side": side,  # "buy" or "sell"
            "type": type,  # "market", "limit", etc.
            "time_in_force": time_in_force  # "day", "gtc", etc.
        }

        response = self._send_request('post', endpoint, data=data)

        if response and 'id' in response:
            return response['id']  # Return the order ID
        else:
            raise Exception("Failed to open position.")

    def close_position(self, symbol, qty, side, type='market', time_in_force='gtc'):
        # For closing a position, you can use similar logic as opening a position
        return self.open_position(symbol, qty, side, type, time_in_force)

