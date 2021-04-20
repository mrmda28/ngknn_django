from rest_framework import serializers
from app_main.models import User_app, Specialty, Group, Teacher, Type, Classroom, Subject, Lesson


class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_app
        fields = ('id', 'username', 'phone', 'building_id')


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'specialty')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('id', 'number', 'name')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'date', 'building_id', 'time', 'duration', 'type_id', 'subject_id', 'group_id', 'teacher_id',
                  'classroom_id')
