from django.db import models
import datetime

class MealCategory(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField(max_length=255)
    code = models.TextField(max_length=10, blank=True)
    order = models.IntegerField(default=0, null=True, blank=True)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"