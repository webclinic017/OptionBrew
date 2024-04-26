# Standard library imports
import datetime
import logging

# Django imports
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Django REST Framework imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, status, permissions
from rest_framework.authtoken.models import Token
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

class UserLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id})
        else:
            return Response({'error': 'Invalid Credentials'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    """
    View to get the current user's details.
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserTransactions(APIView): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        # Fetch transaction details
        ach, direction, timing = request.data.get('transfer_type'), request.data.get('direction'), request.data.get('timing')

        if not ach or not direction or not timing:
            return Response({"Error": "Bad Request. Transaction not completed, at UserTransactions View"}, 
                            status=status.HTTP_400_BAD_REQUEST)

        # Fetch user’s alpaca_account_id
        user = request.user  # Assuming the user is authenticated
        alpaca_account_id = user.alpaca_account_id

        if not alpaca_account_id:
            return Response({"Error": "User does not have an Alpaca account ID set."},
                            status=status.HTTP_404_NOT_FOUND)

        # Perform the transaction or other logic involving the alpaca_account_id
        self._alpaca_fund_request(alpaca_account_id)

        return Response({"Success": "Funds added successfully using Alpaca account ID."}, 
                        status=status.HTTP_200_OK)

          
    def _alpaca_fund_request(self, alpaca_id): 
        