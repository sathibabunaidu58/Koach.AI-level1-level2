
import re
from django.core.exceptions import AppRegistryNotReady
from rest_framework.views import APIView
from rest_framework.response import Response
from new.models import Register
from .serializer import *
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.exceptions import AuthenticationFailed
class SignUpPage(APIView):
    def post(self,request):
        
        serializer = User_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=Register.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('email not exist')
        return Response({'message':'success'})
        


class Home(APIView):
    def get(self,request):
        a=Register.objects.all()
        serialize = User_serializer(a,many=True)
        return Response(serialize.data)
