from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.Address import Address

class AddressSerializer(serializers.ModelSerializer):


    class Meta:
        model = Address
        fields = ['id', 'bulk_address']

        def create(self, validated_data):
            return User.objects.create(**validated_data)