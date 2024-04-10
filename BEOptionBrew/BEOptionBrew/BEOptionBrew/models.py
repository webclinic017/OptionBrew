from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)

    # Override the groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_set_custom",  # Changed related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom",  # Changed related_name
        related_query_name="user_permission",
    )

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
    content = models.TextField()
    mime_type = models.CharField(max_length=50)

class TrustedContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    given_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    email_address = models.EmailField()
