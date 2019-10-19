from django.db import models
import datetime
from ..User import User
from ..models.Menu import Menu


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    rate = models.IntegerField()
    comment = models.TextField(max_length=500, blank=True)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"
        unique_together = (("menu", "user"),)
