from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.MenuDetailsSerializer import MenuDetailsSerializer
from ..serializers.MealSerializer import MealSerializer
from ..models.MenuDetails import MenuDetails


@csrf_exempt
def menu_details_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = MenuDetails.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = MenuDetailsSerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def menu_details_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        menu_details = MenuDetails.objects.get(pk=pk)
    except MenuDetails.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MenuDetailsSerializer(menu_details)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MenuDetailsSerializer(menu_details, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        menu_details.delete()
        return HttpResponse(status=204)


@csrf_exempt
def menu_details_meals(request, pk):
    try:
        lstMeals = list()
        for menudet in MenuDetails.objects.filter(menu=pk):
            lstMeals.append(menudet.meal)

        if request.method == 'GET':
            serializer = MealSerializer(instance=lstMeals, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return None
    except MenuDetails.DoesNotExist:
        return HttpResponse(status=404)
