from django.core.exceptions import ValidationError
from django.http.request import validate_host
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from new.models import Register


class User_serializer(ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
    

class Sign_in(ModelSerializer):
    class Meta:
        model = Register
        fields = ['email','password']
    