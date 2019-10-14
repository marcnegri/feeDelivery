from ..models.Company import Company
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    class Meta:
        app_label = "webapp"