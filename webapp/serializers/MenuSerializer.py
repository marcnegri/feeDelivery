from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.Menu import Menu
from ..models.Review import Review


class MenuSerializer(serializers.ModelSerializer):

    global_review = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'title', 'description', 'availability_date', 'image_url', 'global_review']

        def create(self, validated_data):
            return User.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance

    def get_global_review(self, menu):
        sum = 0
        try:
            lstReviews = Review.objects.filter(menu_id=menu.id)
            for rv in lstReviews:
                sum = sum + rv.rate
            average = sum / len(lstReviews)
            return str(average)
        except:
            return None