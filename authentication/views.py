from ntpath import realpath
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from .models import User
from . import serializers 

# Create your views here.

class helloauthview(generics.GenericAPIView):
  @swagger_auto_schema(operation_summary="Hello Auth")

  def get(self,request):
    return Response({"msg":"HELLO auth"},status=status.HTTP_200_OK)

class UserCreationView(generics.GenericAPIView):
  serializer_class =serializers.UserCreationSerializer
  
  @swagger_auto_schema(operation_summary="create a user account")
  def post(self,request):
    data=request.data

    serializer = self.serializer_class(data=data)

    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data,status=status.HTTP_201_CREATED )

    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


