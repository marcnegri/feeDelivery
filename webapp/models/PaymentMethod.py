from django.db import models
import datetime

class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, blank=False)
    description = models.TextField(max_length=500, blank=True)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"