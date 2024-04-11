from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, unique=True)
    alpaca_account_id = models.CharField(max_length=255, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

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
