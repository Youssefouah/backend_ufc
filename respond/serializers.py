from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail  
#from django.contrib.auth.hashers import check_password
from .exception import expression_errors
import random

message_expression = expression_errors()
message = message_expression.exprission_error()


class UsersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users_extend
        fields = '__all__'

class PutusersSerialiser(serializers.ModelSerializer):
	username=serializers.CharField(max_length=100)
	email=serializers.CharField(max_length=100)
	user=serializers.IntegerField()
	address = serializers.CharField(max_length=100)
	phone = serializers.CharField(max_length=24)


	class Meta:
		model = Users_extend
		fields = ('user','username','email','address','phone')

	def save(self):
		email=self.validated_data['email']
		username=self.validated_data['username']
		user=self.validated_data['user']
		address=self.validated_data['address']
		phone=self.validated_data['phone']
			#if your username is existing get the query of your specific username 
		userd=User.objects.get(id=user)
		userds = Users_extend.objects.get(user=user)
			#then set the new username and email to the existing username
		userd.username=username
		userd.email=email

			#then set the new address and phone to the existing address and phone
		userds.address=address
		userds.phone=phone	

		userd.save()
		userds.save()
		return userd


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email')
        

class RegistrationSerializer(serializers.ModelSerializer):


	class Meta:
		model = User
		fields = ['email', 'username', 'password']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = User(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		account.set_password(password)
		account.save()
		return account


class LoginSerializer(serializers.ModelSerializer):
	username = serializers.CharField()
	class Meta:
		model = User
		fields ='password','username'




class forgot_rest_serializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=100)
	new_password=serializers.CharField(max_length=100)
	old_password=serializers.CharField(max_length=100)

	class Meta:
		model = User
		fields = ['username','new_password','old_password']

	def save(self):
		new_password=self.validated_data['new_password']
		old_password=self.validated_data['old_password']
		username=self.validated_data['username']
		 #filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
		
		if '@' in username:
			try:
				if User.objects.filter(email=username).exists():
					username = User.objects.get(email=username).username	
					#print(username)
					if authenticate(username=username, password= old_password):
						user=User.objects.get(username=username)
						user.set_password(new_password)
						user.save()
						return Response(status=status.HTTP_200_OK)
					else:
						return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
				else:
					return Response(status=status.HTTP_404_NOT_FOUND)		
			except:
				return Response(status=status.HTTP_404_NOT_FOUND)			

	
		elif User.objects.filter(username=username).exists() :
			#print(username)
			if authenticate(username=username, password= old_password):
				user=User.objects.get(username=username)
				user.set_password(new_password)
				user.save()
				return Response(status=status.HTTP_200_OK)
			else :
				return Response(status=status.HTTP_304_NOT_MODIFIED)	

		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

#rest password serializer by email
class rest_serializer(serializers.ModelSerializer):
	email=serializers.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['email']
    
	def sending(self):
		email=self.validated_data['email']
		number = random.randint(1000,9999)
		send_mail(
            'rest password', 
            'this is code : {}'.format(number), 
            'youssefouah1997@gmail.com', 
            [
                email, 
            ]
        ) 
		return number

class rest_serializer_2(serializers.ModelSerializer):
	code=serializers.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['code']
		
	def validation(self):
		code=self.validated_data['code']
		if code == self.sending():
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)


#table scocial_links:
class Sociallinkserialiser(serializers.ModelSerializer):
	class Meta:
		model = Social_url
		fields = '__all__'			

#table cocial links options:
class Social_links_options(serializers.ModelSerializer):
	class Meta:
		model = Social_option
		fields = '__all__'			




