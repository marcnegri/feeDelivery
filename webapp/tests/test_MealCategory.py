from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models.MealCategory import MealCategory
from ..serializers.MealCategorySerializer import MealCategorySerializer


class MealCategoryTest(TestCase):
    """ Test module for MealCategory model """

    def setUp(self):
        MealCategory.objects.create(
            label="Dessert")
        MealCategory.objects.create(
            label='Plats principaux')

    def test_get_all_meal_category(self):
        # get API response
        client = Client()
        response = client.get(reverse('get_all_meal_category'))
        # get data from db
        puppies = MealCategory.objects.all()
        serializer = MealCategorySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)