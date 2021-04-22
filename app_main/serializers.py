from rest_framework import serializers
from app_main.models import User_app, Specialty, Group, Teacher, Classroom, Subject, Lesson, Change


# class UserAppSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User_app
#         fields = ('id', 'username', 'phone', 'building_id')
#

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
#
#
# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = ('id', 'name', 'subject')
#
#
# class ClassroomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classroom
#         fields = ('id', 'number', 'name')
#
#
# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields = ('id', 'name')
#

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'week_day', 'start_time', 'duration', 'subject_id', 'group_id', 'teacher_id',
                  'classroom_id', 'is_top')
#
#
# class ChangeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Change
#         fields = ('id', 'date', 'lesson_id', 'teacher_id', 'subject_id', 'classroom_id', 'is_exists')
