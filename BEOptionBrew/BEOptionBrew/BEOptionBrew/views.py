from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import User, ContactInformation, IdentityInformation, Disclosures, Agreements, Documents, TrustedContact
from .serializers import UserSerializer, ContactInformationSerializer, IdentityInformationSerializer, DisclosuresSerializer, AgreementsSerializer, DocumentsSerializer, TrustedContactSerializer, UserRegistrationSerializer
from .alpaca_broker import Trades
from .alpaca_market import MarketAPI
from django.http import JsonResponse
import datetime
from pytz import timezone
import logging

# Debugging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# User Views
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ContactInformation Views
class ContactInformationListCreate(generics.ListCreateAPIView):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer

class ContactInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer

# IdentityInformation Views
class IdentityInformationListCreate(generics.ListCreateAPIView):
    queryset = IdentityInformation.objects.all()
    serializer_class = IdentityInformationSerializer

class IdentityInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IdentityInformation.objects.all()
    serializer_class = IdentityInformationSerializer

# Disclosures Views
class DisclosuresListCreate(generics.ListCreateAPIView):
    queryset = Disclosures.objects.all()
    serializer_class = DisclosuresSerializer

class DisclosuresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disclosures.objects.all()
    serializer_class = DisclosuresSerializer

# Agreements Views
class AgreementsListCreate(generics.ListCreateAPIView):
    queryset = Agreements.objects.all()
    serializer_class = AgreementsSerializer

class AgreementsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agreements.objects.all()
    serializer_class = AgreementsSerializer

# Documents Views
class DocumentsListCreate(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

class DocumentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer

# TrustedContact Views
class TrustedContactListCreate(generics.ListCreateAPIView):
    queryset = TrustedContact.objects.all()
    serializer_class = TrustedContactSerializer

class TrustedContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrustedContact.objects.all()
    serializer_class = TrustedContactSerializer

# Trades Views
@csrf_exempt  # Only for demo purposes. Make sure to handle CSRF protection properly in production.
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

def live_data_view(request):
    market_api = MarketAPI.get_instance()
    if not market_api.connection or not market_api.connection.sock.connected:
        market_api.connect_to_stream()
        market_api.subscribe_to_stock("TSLA")
        return JsonResponse({"status": "Subscribed to live data", "ticker": "TSLA"})
    else:
        return JsonResponse({"error": "No live data available"}, status=404)

# def market_data_view(request, time_span):
#     market_api = MarketAPI.get_instance()
#     eastern = timezone('US/Eastern')
#     now = datetime.datetime.now(eastern)
#     market_open = datetime.time(9, 30)
#     market_close = datetime.time(16, 0)

#     if market_open <= now.time() <= market_close:
#         # Handle live data when market is open
#         if not market_api.connection or not market_api.connection.sock.connected:
#             market_api.connect_to_stream()
#         market_api.subscribe_to_stock("TSLA")
#         return JsonResponse({"status": "Subscribed to live data", "ticker": "TSLA"})
#     else:
#         # Calculate the date range based on the time_span
#         end_date = now.date()
#         if time_span == '1D':
#             start_date = end_date
#         elif time_span == '1M':
#             start_date = end_date - datetime.timedelta(days=30)
#         elif time_span == '6M':
#             start_date = end_date - datetime.timedelta(days=180)
#         elif time_span == 'YTD':
#             start_date = datetime.date(end_date.year, 1, 1)
#         else:
#             return JsonResponse({'error': 'Invalid time span'}, status=400)

#         data = market_api.fetch_historical_data("TSLA", start_date.isoformat(), end_date.isoformat(), '1D')
#         return JsonResponse(data, safe=False)

#     return JsonResponse({'error': 'Market data request failed'}, status=500)

def historical_data_view(request, time_span):
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

    data = market_api.fetch_historical_data("TSLA", start_date.isoformat(), end_date.isoformat(), '1D')
    return JsonResponse(data, safe=False)