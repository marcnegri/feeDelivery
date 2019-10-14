from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.Meal import Meal
from ..serializers.MealCategorySerializer import MealCategorySerializer

class MealSerializer(serializers.ModelSerializer):
    class Meta:

        meal_category = MealCategorySerializer()

        model = Meal
        fields = ['id', 'title', 'description', 'unit_price', 'image_url', 'meal_category']

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance


