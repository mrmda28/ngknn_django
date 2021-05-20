from rest_framework import serializers

from app_main.models import User_app, Specialty, Group, Teacher, Classroom, Subject, Lesson, Change, Section, Receipt


class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_app
        fields = ('id', 'username', 'phone', 'building', 'is_admin')


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id', 'name', 'image')


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


class ChangeSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Change
        fields = ('id', 'date', 'lesson', 'start_time', 'duration', 'subject', 'teacher', 'classroom')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'image', 'url')


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'group', 'student', 'birthday', 'quantity', 'where', 'military_commissariat', 'is_active')
