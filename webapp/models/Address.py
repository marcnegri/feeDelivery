from django.db import models
from ..models.Company import Company
import datetime

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    bulk_address = models.TextField(max_length=500, blank=False)
    street_number = models.TextField(max_length=10, blank=True)
    street = models.TextField(max_length=255, blank=True)
    street_2 = models.TextField(max_length=255, blank=True)
    zip_code = models.TextField(max_length=10, blank=True)
    country = models.TextField(max_length=50, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)


    class Meta:
        app_label = "webapp"