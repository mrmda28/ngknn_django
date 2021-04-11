from rest_framework import serializers
from app_main.models import User_app, Specialty, Group


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
        fields = ('id', 'name', 'specialty_id')
