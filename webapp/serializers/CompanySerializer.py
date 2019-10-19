from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.Company import Company
from ..models.Address import Address
from .AddressSerializer import AddressSerializer

class CompanySerializer(serializers.ModelSerializer):

    addresses = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'label', 'description', 'access_code', 'bill_participation', 'addresses']

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance

    def get_addresses(self, company):
        try:
            addresses = Address.objects.filter(company_id=company.id)
            return AddressSerializer(addresses, many=True).data
        except:
            return None