from webapp.models.Company import Company
from webapp.models.Address import Address
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    email = models.EmailField(('email address'), unique=True)
    delivery_address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None)
    payment_service_id = models.TextField(default='', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        app_label = "webapp"