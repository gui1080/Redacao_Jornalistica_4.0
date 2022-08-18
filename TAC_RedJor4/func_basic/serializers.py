from rest_framework import serializers
from .models import User_Login

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Login
        fields = ('id', 'name', 'password', 'email')