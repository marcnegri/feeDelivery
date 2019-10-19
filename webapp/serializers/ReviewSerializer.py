from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.Review import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'comment', 'rate', 'user', 'menu']

        def create(self, validated_data):
            return User.objects.create(**validated_data)