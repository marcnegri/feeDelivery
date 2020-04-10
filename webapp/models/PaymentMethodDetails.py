from django.db import models
from ..models.PaymentMethod import PaymentMethod
from ..User import User
import datetime

class PaymentMethodDetails(models.Model):
    id = models.AutoField(primary_key=True)
    related_service_token = models.TextField(max_length=500, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"