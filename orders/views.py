from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from . import  serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.shortcuts import  get_object_or_404
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

User=get_user_model()


class helloordersview(generics.GenericAPIView):
  @swagger_auto_schema(operation_summary="Hello Order")

  def get(self,request):
    return Response({"msg":"HELLO orders"},status=status.HTTP_200_OK)



class orderCreateView(generics.GenericAPIView):
  
  queryset = order.objects.all()
  serializer_class = serializers.orderCreationSerialzer
  permission_classes = [IsAuthenticatedOrReadOnly]

  @swagger_auto_schema(operation_summary="List All Orders Made")

  def get(self,request):
    orders= order.objects.all()
    serializer= self.serializer_class(instance=orders, many=True)

    return Response(data=serializer.data,status=status.HTTP_200_OK)

  @swagger_auto_schema(operation_summary="create An Order")

  def post(self,request):
    data =request.data

    serializer= self.serializer_class(data=data)
    user = request.user

    if serializer.is_valid():
      serializer.save(customer=user)
      return Response(data= serializer.data,status=status.HTTP_201_CREATED)
    return Response(data = serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class orderDetailView(generics.GenericAPIView):
  serializer_class = serializers.orderUpdateSerialzer
  permission_classes = [IsAdminUser]
  @swagger_auto_schema(operation_summary="Retrieve All Orders")

  def get(self,request,order_id):    
    orders=get_object_or_404(order,pk=order_id)
    serializer = self.serializer_class(instance=orders)
    return Response(data=serializer.data,status=status.HTTP_200_OK) 

  @swagger_auto_schema(operation_summary="Update An Order")

  def put(self,request,order_id):
    data = request.data

    orders = get_object_or_404(order,pk=order_id)

    serializer =self.serializer_class(data=data,instance=orders)

    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # user= request.user
    # serializer=self.serializer_class(data=data)

    # if serializer.is_valid():
    #   serializer.save(customer=user)

    #   return Response(data=serializer.data,status=status.HTTP_200_OK)

    # return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
  @swagger_auto_schema(operation_summary="Delete/Remove an Order")

  def delete(self,request,order_id):

    orders= get_object_or_404(order,pk=order_id)

    orders.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateOrderStatus(generics.GenericAPIView):
  serializer_class=serializers.Orderstatusupdateserializer
  permission_classes = [IsAdminUser]
  @swagger_auto_schema(operation_summary="Update an Order's Status")
 
  def put(self,request,order_id):
    orders = get_object_or_404(order,pk=order_id)

    data=request.data

    serializer=self.serializer_class(data=data,instance=orders)

    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserOrdersView(generics.GenericAPIView):
  serializer_class=serializers.orderUpdateSerialzer
  @swagger_auto_schema(operation_summary="Get a User's all Orders")

  def get(self,request,user_id):
    user = User.objects.get(pk=user_id)
    orders=order.objects.all().filter(customer=user)
    serializer=self.serializer_class(instance=orders,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


class  userOrderDetialsView(generics.GenericAPIView):
  serializer_class=serializers.orderUpdateSerialzer
  @swagger_auto_schema(operation_summary="Get User's Specific Order")

  def get(self,request,user_id,order_id):
    user = User.objects.get(pk=user_id)
    orders=order.objects.all().filter(customer=user).get(pk=order_id)
    serializer=self.serializer_class(instance=orders)
    return Response(data=serializer.data,status=status.HTTP_200_OK)
