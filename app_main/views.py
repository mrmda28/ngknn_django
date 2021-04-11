import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_main.models import Token, User_app, Building, Specialty, Group, Teacher
from app_main.serializers import UserAppSerializer, SpecialtySerializer, GroupSerializer


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

                return Response(json_token, status=status.HTTP_200_OK)
            else:
                return Response('ERROR: Invalid password', status=status.HTTP_403_FORBIDDEN)
        return Response('ERROR: User not found', status=status.HTTP_404_NOT_FOUND)


# --------- Create or get users-app --------- #
@api_view(['POST', 'GET'])
def api_users_app(request):
    # If http method is POST, then the user-app will be created
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
            t = Token.objects.create(token=token,user=user)
            t.save()
            json_token = {'token': token}

            return Response(json_token, status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: User already exists', status=status.HTTP_409_CONFLICT)

    # If http method is GET, then all users will be returned
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            users = User_app.objects.all()
            serializer = UserAppSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('ERROR: Access is denied', status=status.HTTP_401_UNAUTHORIZED)


# --------- Get specialties --------- #
@api_view(['GET'])
def api_specialty(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            specialties = Specialty.objects.all()
            serializer = SpecialtySerializer(specialties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('ERROR: Access is denied', status=status.HTTP_401_UNAUTHORIZED)


# --------- Get groups --------- #
@api_view(['GET'])
def api_group(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('ERROR: Access is denied', status=status.HTTP_401_UNAUTHORIZED)


# --------- Creat or get teachers --------- #
@api_view(['POST', 'GET'])
def api_teacher(request):
    # If http method is POST, then the teacher will be created
    if request.method == 'POST':
        if not Teacher.objects.filter(name=request.data['name']):

            teacher = Teacher.objects.create(name=request.data['name'])
            teacher.save()

            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: Teacher already exists', status=status.HTTP_409_CONFLICT)

    # If http method is GET, then all teachers will be returned
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            teachers = Teacher.objects.all()
            serializer = GroupSerializer(teachers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('ERROR: Access is denied', status=status.HTTP_401_UNAUTHORIZED)
