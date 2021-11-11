from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TaskModel

class UserSerializer(serializers.ModelSerializer):
    """Serializer For User Model"""
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class TaskSerializer(serializers.ModelSerializer):
    """Serializer For Task Model"""
    class Meta:
        """ Serialize All Feilds"""
        model = TaskModel
        fields = '__all__'
