from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..serializers.CompanySerializer import CompanySerializer
from ..models.Company import Company


@csrf_exempt
def company_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        user = Company.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = CompanySerializer(user, many=True, context=serializer_context)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def company_details(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CompanySerializer(company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        company.delete()
        return HttpResponse(status=204)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def company_discount(request, pk=0):
    try:
        if pk == 0 and request.user.is_authenticated:
            pk = request.user.company.id

        comp = Company.objects.get(pk=pk)
        return HttpResponse(comp.bill_participation)
    except Company.DoesNotExist:
        return HttpResponse(status=404)

class CompanyList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Company.objects.all()
        access_code = self.request.query_params.get('access_code', None)
        try:
            if access_code is not None:
                queryset = queryset.filter(access_code=access_code)

            if self.request.method == 'GET':
                return queryset
        except Company.DoesNotExist:
            return HttpResponse(status=404)
