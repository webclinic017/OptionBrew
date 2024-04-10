from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    # You can add more fields as needed

class ContactInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)

class IdentityInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    given_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    country_of_tax_residence = models.CharField(max_length=3)
    funding_source = models.CharField(max_length=255)

class Disclosures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_control_person = models.BooleanField()
    is_affiliated_exchange_or_finra = models.BooleanField()
    is_politically_exposed = models.BooleanField()
    immediate_family_exposed = models.BooleanField()

class Agreements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agreement_type = models.CharField(max_length=255)
    signed_at = models.DateTimeField()
    ip_address = models.CharField(max_length=255)

class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=255)
    document_sub_type = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()  # Consider changing to a FileField or similar if storing files
    mime_type = models.CharField(max_length=50)

class TrustedContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    given_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    email_address = models.EmailField()
