from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import (
    User, ContactInformation, IdentityInformation, Disclosures,
    Agreements, Documents, TrustedContact
)
from .serializers import (
    UserSerializer, ContactInformationSerializer, IdentityInformationSerializer,
    DisclosuresSerializer, AgreementsSerializer, DocumentsSerializer,
    TrustedContactSerializer, UserRegistrationSerializer
)

from .alpaca_broker import Trades

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
        data = request.POST  # Assuming you're sending data via POST request
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