from django.db import models
from django.contrib.auth.models import User
from ..models.MealCategory import MealCategory
import datetime


class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, blank=False)
    description = models.TextField(max_length=500, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    unit_price = models.FloatField(blank=False)
    meal_category = models.ForeignKey(MealCategory, on_delete=models.CASCADE, default=3)
    updating_date = models.DateTimeField(default=datetime.datetime.now)
    inserting_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        app_label = 'webapp'
        verbose_name = 'meal'
        verbose_name_plural = 'meals'
