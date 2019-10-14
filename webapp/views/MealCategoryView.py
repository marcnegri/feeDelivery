from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.MealCategorySerializer import MealCategorySerializer
from ..models.MealCategory import MealCategory


@csrf_exempt
def meal_category_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = MealCategory.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = MealCategorySerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MealCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def meal_category_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        company = MealCategory.objects.get(pk=pk)
    except MealCategory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MealCategorySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MealCategorySerializer(company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)