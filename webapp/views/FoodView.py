from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.FoodSerializer import FoodSerializer
from ..models.Food import Food


@csrf_exempt
def food_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = Food.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = FoodSerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def food_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FoodSerializer(food, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        food.delete()
        return HttpResponse(status=204)