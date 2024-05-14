# Standard library imports
import datetime
import logging

# Django imports
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Django REST Framework imports
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Third-party imports
from pytz import timezone

# Local application imports
from ..models import (
    User, ContactInformation, IdentityInformation, Disclosures, 
    Agreements, Documents, TrustedContact
)
from ..serializers import (
    UserSerializer, ContactInformationSerializer, IdentityInformationSerializer, 
    DisclosuresSerializer, AgreementsSerializer, DocumentsSerializer, 
    TrustedContactSerializer, UserRegistrationSerializer
)
from ..alpaca_broker import Trades
from ..alpaca_market import MarketAPI

# Data Views
@csrf_exempt  # Only for demo purposes.
def open_position_view(request):
    if request.method == 'POST':
        data = request.POST  
        symbol = data.get('symbol')
        qty = data.get('qty')
        side = data.get('side')
        
        trades = Trades()
        try:
            order_id = trades.open_position(symbol, qty, side)
            return JsonResponse({'order_id': order_id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:


        return JsonResponse({'error': 'Method not allowed'}, status=405)

def is_market_open():
    eastern = timezone('US/Eastern')
    now = datetime.datetime.now(eastern)
    market_open = datetime.time(9, 30)
    market_close = datetime.time(16, 0)
    return market_open <= now.time() <= market_close

def get_live_data(request, ticker):
    """Endpoint to get the latest live data for a ticker."""
    market_api = MarketAPI.get_instance()
    data = market_api.data.get(ticker, [])
    if data:
        # Return the last few entries, e.g., the last 10 entries
        return JsonResponse(data[-10:], safe=False)
    else:
        return JsonResponse({"error": "No data available for the specified ticker"}, status=404)

def live_data_view(request, ticker):
    market_api = MarketAPI.get_instance()
    if not market_api.connection or not market_api.connection.sock.connected:
        market_api.connect_to_stream()
    market_api.subscribe_to_stock(ticker)
    return JsonResponse({"status": "Subscribed to live data", "ticker": ticker})

def historical_data_view(request, ticker, time_span):
    market_api = MarketAPI.get_instance()
    eastern = timezone('US/Eastern')
    now = datetime.datetime.now(eastern)
    end_date = now.date()

    # Calculate start date based on time_span
    if time_span == '1D':
        start_date = end_date
    elif time_span == '1M':
        start_date = end_date - datetime.timedelta(days=30)
    elif time_span == '6M':
        start_date = end_date - datetime.timedelta(days=180)
    elif time_span == 'YTD':
        start_date = datetime.date(end_date.year, 1, 1)
    else:
        return JsonResponse({'error': 'Invalid time span'}, status=400)

    data = market_api.fetch_historical_data(ticker, start_date.isoformat(), end_date.isoformat(), '1D')
    print(data)
    return JsonResponse(data, safe=False)
