from rest_framework import serializers
from .models import user_register

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_register
        fields = ['id', 'name', 'email', 'password', 'con_password',]
