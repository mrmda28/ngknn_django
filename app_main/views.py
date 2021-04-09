import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Token, User_app, Building


def get_hash_password(password):
    salt = b'ngknn'
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(str.encode(password))
    digest.update(salt)
    return digest.finalize()


# --------- User authorization --------- #
@api_view(['POST'])
def api_auth(request):
    if request.method == 'POST':
        if User_app.objects.filter(phone=request.data['phone']):
            user_app = User_app.objects.get(phone=request.data['phone'])

            password_hash = str(get_hash_password(request.data['password']))

            if user_app.password == password_hash:
                token = Token.objects.get(user=user_app)
                json_token = {'token': token.token}

                return JsonResponse(json_token, status=status.HTTP_200_OK, safe=False)
            else:
                return JsonResponse('ERROR: Invalid password', status=status.HTTP_403_FORBIDDEN, safe=False)
        return JsonResponse('ERROR: User not found', status=status.HTTP_404_NOT_FOUND, safe=False)


# --------- User registration --------- #
@api_view(['POST'])
def api_create_user_app(request):
    if request.method == 'POST':
        if not User_app.objects.filter(phone=request.data['phone']):
            building = Building.objects.get(number=request.data['building'])
            password = get_hash_password(request.data['password'])

            user_app = User_app.objects.create(username=request.data['username'],
                                               phone=request.data['phone'],
                                               password=password,
                                               building=building)
            user_app.save()

            user = User_app.objects.get(username=request.data['username'])
            token = str(secrets.token_urlsafe())
            t = Token.objects.create(token=token,
                                     user=user)
            t.save()
            json_token = {'token': token}

            return JsonResponse(json_token, status=status.HTTP_201_CREATED, safe=False)
        else:
            return JsonResponse('ERROR: User already exists', status=status.HTTP_409_CONFLICT, safe=False)
