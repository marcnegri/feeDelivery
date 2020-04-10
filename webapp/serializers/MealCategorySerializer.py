from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.MealCategory import MealCategory

class MealCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = ['id', 'label', 'code']

        def create(self, validated_data):
            return User.objects.create(**validated_data)