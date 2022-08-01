from dataclasses import fields
from email.policy import default
from .models import order
from rest_framework import serializers

# class userorderdetailsseriaizer(serializers.ModelSerializer):
#   class Meta:
#     model= order
#     fields =['customer']

class orderCreationSerialzer(serializers.ModelSerializer):
  size = serializers.CharField(max_length=20)
  order_status = serializers.HiddenField(default='PENDING')
  quantity = serializers.IntegerField()

  class Meta:
    model = order
    fields = ['id','size','order_status','quantity']

  

class orderUpdateSerialzer(serializers.ModelSerializer):
  
  size = serializers.CharField(max_length=20)
  order_status = serializers.CharField(default='PENDING')
  quantity = serializers.IntegerField()
  created_at = serializers.DateField()
  updated_at = serializers.DateField()


  class Meta:
    model = order
    fields = ['customer','id','size','order_status','quantity','created_at','updated_at']

class Orderstatusupdateserializer(serializers.ModelSerializer):
  order_status = serializers.CharField(default='PENDING')

  class Meta:
    model=order
    fields = ['order_status']