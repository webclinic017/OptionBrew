from rest_framework import serializers
from django.db import transaction
from .models import User, ContactInformation, IdentityInformation, Disclosures, Agreements, Documents, TrustedContact

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

class UserRegistrationSerializer(serializers.Serializer):
    user = UserSerializer()
    contact_information = ContactInformationSerializer()
    identity_information = IdentityInformationSerializer()
    disclosures = DisclosuresSerializer()
    agreements = AgreementsSerializer(many=True)
    documents = DocumentsSerializer(many=True)
    trusted_contact = TrustedContactSerializer()

    @transaction.atomic
    def create(self, validated_data):
        # Create the user first
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.get('password'))  # Ensure 'password' key exists
        user.save()

        # Create related objects without the 'user' field explicitly
        ContactInformation.objects.create(user=user, **validated_data.pop('contact_information'))
        IdentityInformation.objects.create(user=user, **validated_data.pop('identity_information'))
        Disclosures.objects.create(user=user, **validated_data.pop('disclosures'))

        # Agreements and documents can have multiple instances, so iterate through them
        for agreement_data in validated_data.pop('agreements'):
            Agreements.objects.create(user=user, **agreement_data)
        
        for document_data in validated_data.pop('documents'):
            Documents.objects.create(user=user, **document_data)

        TrustedContact.objects.create(user=user, **validated_data.pop('trusted_contact'))

        return user
