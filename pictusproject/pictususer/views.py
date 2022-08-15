from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import views
from rest_framework.views import APIView


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class=LoginSerializer

    def post(self, request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"message":"로그인 성공", 'data':serializer.data})
        return Response({"message":"로그인 실패",'error':serializer.errors})

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

class ProfileListView(views.APIView):
    def get(self, request, format=None):
        profile=Profile.objects.all()
        serializer=ProfileListSerializer(profile, many=True)
        return Response(serializer.data)



    

