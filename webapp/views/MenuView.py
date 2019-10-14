from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ..serializers.MenuSerializer import MenuSerializer
from ..models.Menu import Menu


@csrf_exempt
def menu_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = Menu.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = MenuSerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def menu_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(menu, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        menu.delete()
        return HttpResponse(status=204)