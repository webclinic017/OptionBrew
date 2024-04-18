from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.hashers import make_password
from .models import User, ContactInformation, IdentityInformation, Disclosures, Agreements, Documents, TrustedContact
from .alpaca_broker import Users as AlpacaUsers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number']

class ContactInformationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = ContactInformation
        fields = '__all__'

class IdentityInformationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = IdentityInformation
        fields = '__all__'

class DisclosuresSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Disclosures
        fields = '__all__'

class AgreementsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Agreements
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Documents
        fields = '__all__'

class TrustedContactSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = TrustedContact
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'alpaca_account_id']  # Added 'alpaca_account_id'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number']

    def create(self, validated_data):
        # Hash the user's password
        validated_data['password'] = make_password(validated_data.pop('password'))

        # Check if a user with the provided phone number already exists
        phone_number = validated_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError("Phone number is already in use.")

        # Create the user instance
        user = User.objects.create(**validated_data)

        # Call Alpaca API to register the user
        alpaca_api = AlpacaUsers()
        alpaca_account_id = alpaca_api.registerUser(user.first_name, user.last_name, user.email, user.phone_number)
        user.alpaca_account_id = alpaca_account_id
        user.save()  # Save the user instance after updating it

        return user

