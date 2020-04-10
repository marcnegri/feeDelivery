from ..User import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..serializers.UserSerializer import UserSerializer
from ..serializers.UserSerializer import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        try:
            if 'HTTP_AUTHORIZATION' in request.META:
                oauth_token = request.META['HTTP_AUTHORIZATION'].split()[1]
                oauth_obj = Token.objects.get(key=oauth_token)
                user = User.objects.all()
                serializer_context = {
                    'request': request,
                }
                serializer = UserSerializer(user, many=True, context=serializer_context)
                return JsonResponse(serializer.data, safe=False)
            else:
                HttpResponse(status=404)
        except Token.DoesNotExist:
            return HttpResponse(status=404)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.create(data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk=0):
    """
    Retrieve, update or delete a user.
    """
    try:
        if pk == 0 and request.user.is_authenticated:
            user = request.user
        else:
            user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET'])
def user_detail_by_email(request, _email):
    """
    Retrieve, update or delete a user.
    """
    try:
        #tokenCode = request.META['HTTP_AUTHORIZATION']
        user = User.objects.get(email=_email)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)