from django.db import models
import datetime
from ..models.Menu import Menu
from ..models.Meal import Meal


class MenuDetails(models.Model):
    id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, default=None, related_name='meals')
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = "webapp"
