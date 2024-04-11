from rest_framework import generics, status
from rest_framework.response import Response
from .models import (
    User, ContactInformation, IdentityInformation, Disclosures,
    Agreements, Documents, TrustedContact
)
from .serializers import (
    UserSerializer, ContactInformationSerializer, IdentityInformationSerializer,
    DisclosuresSerializer, AgreementsSerializer, DocumentsSerializer,
    TrustedContactSerializer, UserRegistrationSerializer
)

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
