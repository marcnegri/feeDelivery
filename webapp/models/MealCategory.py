from django.db import models
import datetime

class MealCategory(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField(max_length=255)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"