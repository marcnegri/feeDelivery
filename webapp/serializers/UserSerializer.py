from rest_framework import serializers
from ..serializers.CompanySerializer import CompanySerializer
from ..serializers.AddressSerializer import AddressSerializer
from ..User import User
from ..models.Company import Company
from ..models.Address import Address

class UserSerializer(serializers.ModelSerializer):

    company = CompanySerializer()
    delivery_address = AddressSerializer()

    class Meta:
        model = User
        depth = 2
        fields = ['username', 'first_name', 'last_name', 'id',
                   'is_active', 'id', 'email', 'company', 'delivery_address',
                  'payment_service_id']

    def create(self, validated_data):

        company = validated_data.pop('company')
        delivery_address = validated_data.pop('delivery_address')
        fakeIdUser = validated_data.pop('id')
        user = User.objects.create(**validated_data, company=Company.objects.get(id=company['id']),
                                   delivery_address=Address.objects.get(id=delivery_address['id']))
        user.set_password(user.password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def get_company_object(self, user):
        try:
            return CompanySerializer(user.company).data
        except:
            return None

    def get_delivery_address(self, user):
        try:
            return AddressSerializer(user.delivery_address).data
        except:
            return None