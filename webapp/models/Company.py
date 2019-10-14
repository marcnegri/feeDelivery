from django.db import models
import datetime

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField(max_length=255, blank=False)
    description = models.TextField(max_length=500, blank=True)
    access_code = models.CharField(max_length=8, blank=False)
    bill_participation = models.IntegerField(blank=False)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"