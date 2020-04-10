from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.MealSerializer import MealSerializer
from ..models.Meal import Meal


@csrf_exempt
def meal_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = Meal.objects.all()

        serializer_context = {
            'request': request,
        }
        serializer = MealSerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MealSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def meal_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        meal = Meal.objects.get(pk=pk)
    except Meal.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MealSerializer(meal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MealSerializer(meal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        meal.delete()
        return HttpResponse(status=204)