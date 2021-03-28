import secrets

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Token, User_app, Building


@api_view(['POST'])
def api_auth(request):
    if request.method == 'POST':
        user_app = User_app.objects.get(phone=request.data['phone'])

        if user_app.password != request.data['password']:
            return JsonResponse('ERROR: Invalid password', status=status.HTTP_400_BAD_REQUEST, safe=False)
        else:
            token = Token.objects.get(user=user_app)
            json_token = {'token': token.token}

            return JsonResponse(json_token, status=status.HTTP_201_CREATED, safe=False)


@api_view(['POST'])
def api_create_user_app(request):
    if request.method == 'POST':
        building = Building.objects.get(number=request.data['building'])

        user_app = User_app.objects.create(username=request.data['username'],
                                           phone=request.data['phone'],
                                           password=request.data['password'],
                                           building=building)
        user_app.save()

        user = User_app.objects.get(username=request.data['username'])
        token = str(secrets.token_urlsafe())
        t = Token.objects.create(token=token,
                                 user=user)
        t.save()
        json_token = {'token': token}

        return JsonResponse(json_token, status=status.HTTP_201_CREATED, safe=False)
    return JsonResponse('Error', status=status.HTTP_400_BAD_REQUEST, safe=False)
