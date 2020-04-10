from hashlib import md5

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from ..serializers.MealSerializer import MealSerializer
from ..models.Meal import Meal
from django.conf import settings
import stripe

@csrf_exempt
def init_stripe_connection():
    """
    Connection to a stripe API service
    """

    charge = stripe.Charge.retrieve(
      "ch_1GAI43JD6p90qphN1DUjPaUa",
      api_key="sk_test_wUdns0vRLjMj2ajUVYCcFEtN00rJ5U4QcJ"
    )
    charge.save()

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def create_stripe_customer(request):
    try:
        if request.user.is_authenticated:
            stripe.api_key = settings.API_STRIPE_SECRET_KEY
            response = stripe.Customer.create(description=md5(request.user.email.encode()).hexdigest())
            return HttpResponse(response)
        else:
            return HttpResponse(status=500)
    except:
        #TODO : Log Error from API
        return HttpResponse(status=500)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_credit_card(request):
    try:
        if request.user.is_authenticated:
            stripe.api_key = settings.API_STRIPE_SECRET_KEY
            token = stripe.Token.create(card={"number": "4242424242424242", "exp_month": 2, "exp_year": 2021, "cvc": "314", } )
            if token is not None:
                response = stripe.Customer.create_source(request.user.payment_service_id, source=token)
                return HttpResponse(response)
        else:
            return HttpResponse(status=500)
    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught

        print('Status is: %s' % e.http_status)
        print('Type is: %s' % e.error.type)
        print('Code is: %s' % e.error.code)
        # param is '' in this case
        print('Param is: %s' % e.error.param)
        print('Message is: %s' % e.error.message)
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        pass
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        print('Status is: %s' % e.http_status)
        print('Type is: %s' % e.error.type)
        print('Code is: %s' % e.error.code)
        # param is '' in this case
        print('Param is: %s' % e.error.param)
        print('Message is: %s' % e.error.message)
        return HttpResponse(status=500)
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        pass
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        pass
    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        pass
    except Exception as e:
        print('Message is: %s' % e.error.message)
        # Something else happened, completely unrelated to Stripe
        pass