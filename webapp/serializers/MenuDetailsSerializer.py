from rest_framework import serializers
from ..models.MenuDetails import MenuDetails
from ..serializers.MenuSerializer import MenuSerializer
from ..serializers.MealSerializer import MealSerializer

class MenuDetailsSerializer(serializers.ModelSerializer):

    meals = serializers.SerializerMethodField()

    class Meta:
        model = MenuDetails
        fields = ['id', 'meals']

    def create(self, validated_data):
        return MenuDetails.objects.create(**validated_data)

    def get_meals(self, menuDetails):
        try:
            lstMeals = []
            for menudet in MenuDetails.objects.all():
                lstMeals.append(menudet.meal)

            return MealSerializer(lstMeals, many=True).data
        except:
            return None