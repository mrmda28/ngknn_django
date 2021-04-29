import secrets

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_main.models import Token, User_app, Building, Specialty, Group, Teacher, Classroom, Subject, Lesson
from app_main.serializers import UserAppSerializer, SpecialtySerializer, GroupSerializer, TeacherSerializer, \
    ClassroomSerializer, SubjectSerializer, LessonSerializer


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
def api_users_app(request, pk=None):
    if request.method == 'POST':
        if not User_app.objects.filter(phone=request.data['phone']):
            password = get_hash_password(request.data['password'])

            user_app = User_app.objects.create(username=request.data['username'],
                                               phone=request.data['phone'],
                                               password=password,
                                               building=Building.objects.get(id=request.data['building']))
            user_app.save()

            user = User_app.objects.get(username=request.data['username'])
            token = str(secrets.token_urlsafe())
            t = Token.objects.create(token=token, user=user)
            t.save()
            json_token = {'token': token}

            return Response(json_token, status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: User already exists', status=status.HTTP_409_CONFLICT)

    if request.method == 'GET':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            if pk is not None:
                if User_app.objects.filter(pk=pk).exists():
                    user = User_app.objects.filter(pk=pk)
                    serializer = UserAppSerializer(user, many=True)

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response('ERROR: User not found', status=status.HTTP_404_NOT_FOUND)
            else:
                users = User_app.objects.all()
                serializer = UserAppSerializer(users, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('ERROR: Access is denied', status=status.HTTP_401_UNAUTHORIZED)


# --------- Create or get specialties --------- #
@api_view(['POST', 'GET'])
def api_specialty(request, pk=None):
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            if not Specialty.objects.filter(name=request.data['name']):
                specialty = Specialty.objects.create(name=request.data['name'])
                specialty.save()

                return Response('SUCCESS', status=status.HTTP_201_CREATED)
            else:
                return Response('ERROR: Specialty already exists', status=status.HTTP_409_CONFLICT)

    if request.method == 'GET':
        if pk is None:
            specialties = Specialty.objects.all()
            serializer = SpecialtySerializer(specialties, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if Specialty.objects.filter(pk=pk).exists():
                if Group.objects.filter(specialty=pk).exists():
                    groups = Group.objects.filter(specialty=pk)
                    serializer = GroupSerializer(groups, many=True)

                    specialty = Specialty.objects.get(pk=pk)

                    response = {'name': specialty.name,
                                'groups': serializer.data}

                    return Response(response, status=status.HTTP_200_OK)
                else:
                    return Response('ERROR: Groups not found', status=status.HTTP_404_NOT_FOUND)
            else:
                return Response('ERROR: Specialty not found', status=status.HTTP_404_NOT_FOUND)


# --------- Creat or get lessons --------- #
@api_view(['POST', 'GET'])
def api_lesson(request, pk_group=None, pk_week_day=None):
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            if not Lesson.objects.filter(week_day=request.data['week_day'],
                                         start_time=request.data['start_time'],
                                         duration=request.data['duration'],
                                         group=request.data['group'],
                                         is_top=request.data['is_top'],
                                         subject=request.data['subject'],
                                         teacher=request.data['teacher'],
                                         classroom=request.data['classroom']).exists():
                lesson = Lesson.objects.create(week_day=request.data['week_day'],
                                               start_time=request.data['start_time'],
                                               duration=request.data['duration'],
                                               group=Group.objects.get(id=request.data['group']),
                                               is_top=request.data['is_top'],
                                               subject=Subject.objects.get(id=request.data['subject']),
                                               teacher=Teacher.objects.get(id=request.data['teacher']),
                                               classroom=Classroom.objects.get(id=request.data['classroom']))
                lesson.save()

                return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: Access is denied', status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        if (pk_group and pk_week_day) is not None:
            lesson_by_group_week_day = Lesson.objects.filter(group=pk_group, week_day=pk_week_day)
            serializer = LessonSerializer(lesson_by_group_week_day, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        elif pk_group is not None:
            lesson_by_group = Lesson.objects.filter(group=pk_group)
            serializer = LessonSerializer(lesson_by_group, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        elif (pk_group and pk_week_day) is None:
            lessons = Lesson.objects.all()
            serializer = LessonSerializer(lessons, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('ERROR: Incorrect request', status=status.HTTP_400_BAD_REQUEST)


# --------- Create or get groups --------- #
@api_view(['POST', 'GET'])
def api_group(request, pk=None):
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if Token.objects.filter(token=token).exists():
            if not Group.objects.filter(name=request.data['name']):
                group = Group.objects.create(name=request.data['name'],
                                             specialty=Specialty.objects.get(id=request.data['specialty']))
                group.save()

                return Response('SUCCESS', status=status.HTTP_201_CREATED)
            else:
                return Response('ERROR: Group already exists', status=status.HTTP_409_CONFLICT)

    if request.method == 'GET':
        if pk is not None:
            if Group.objects.filter(pk=pk).exists():
                group = Group.objects.filter(pk=pk)
                serializer = GroupSerializer(group, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('ERROR: Group not found', status=status.HTTP_404_NOT_FOUND)
        else:
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)


# --------- Creat or get teachers --------- #
@api_view(['POST', 'GET'])
def api_teacher(request, pk=None):
    if request.method == 'POST':
        if not Teacher.objects.filter(name=request.data['name']):

            teacher = Teacher.objects.create(name=request.data['name'])
            teacher.save()

            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: Teacher already exists', status=status.HTTP_409_CONFLICT)

    if request.method == 'GET':
        if pk is not None:
            if Teacher.objects.filter(pk=pk).exists():
                teacher = Teacher.objects.filter(pk=pk)
                serializer = TeacherSerializer(teacher, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('ERROR: Teacher not found', status=status.HTTP_404_NOT_FOUND)
        else:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)


# --------- Creat or get classrooms --------- #
@api_view(['POST', 'GET'])
def api_classroom(request, pk=None):
    if request.method == 'POST':
        if not Classroom.objects.filter(number=request.data['number']):

            classroom = Classroom.objects.create(number=request.data['number'],
                                                 name=request.data['name'])
            classroom.save()

            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: Classroom already exists', status=status.HTTP_409_CONFLICT)

    if request.method == 'GET':
        if pk is not None:
            if Classroom.objects.filter(pk=pk).exists():
                classroom = Classroom.objects.filter(pk=pk)
                serializer = ClassroomSerializer(classroom, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('ERROR: Classroom not found', status=status.HTTP_404_NOT_FOUND)
        else:
            classrooms = Classroom.objects.all()
            serializer = ClassroomSerializer(classrooms, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)


# --------- Creat or get subject --------- #
@api_view(['POST', 'GET'])
def api_subject(request, pk=None):
    if request.method == 'POST':
        if not Subject.objects.filter(name=request.data['name']):

            subject = Subject.objects.create(name=request.data['name'])
            subject.save()

            return Response('SUCCESS', status=status.HTTP_201_CREATED)
        else:
            return Response('ERROR: Subject already exists', status=status.HTTP_409_CONFLICT)

    if request.method == 'GET':
        if pk is not None:
            if Subject.objects.filter(pk=pk).exists():
                subject = Subject.objects.filter(pk=pk)
                serializer = SubjectSerializer(subject, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('ERROR: Subject not found', status=status.HTTP_404_NOT_FOUND)
        else:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
