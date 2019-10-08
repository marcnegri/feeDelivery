from django.db import models
from django.contrib.auth.models import User
import datetime

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, blank=False)
    description = models.TextField(max_length=500, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    unit_price = models.FloatField(blank=False)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)


    class Meta:
        app_label = "webapp"