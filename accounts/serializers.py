from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import UserAccount
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    bio = serializers.CharField(required=False)
    avatar = serializers.ImageField(required=False)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'phone_number', 'username', 'bio', 'avatar')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name', 'phone_number',
            'bio', 'avatar', 'is_active', 'is_staff'
        )
