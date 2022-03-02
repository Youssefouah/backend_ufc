from attr import fields
from rest_framework import serializers
from . models import users




class UsersSerialiser(serializers.ModelSerailizer):
     class Meta:
         model = users
         fields = '__all__'








