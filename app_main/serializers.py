from rest_framework import serializers

from app_main.models import User_app, Specialty, Group, Teacher, Classroom, Subject, Lesson


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
        fields = ('id', 'name')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
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
    group = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Lesson
        fields = ('id', 'week_day', 'start_time', 'duration', 'group', 'is_top', 'subject', 'teacher', 'classroom')
