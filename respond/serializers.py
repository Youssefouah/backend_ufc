import code
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
from .signale import Signal_code
import random


code = {}




class UsersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users_extended
        fields = ('id','job','address','phone','created_At','updated_At')

class PutusersSerialiser(serializers.ModelSerializer):
	username=serializers.CharField(max_length=100)
	email=serializers.CharField(max_length=100)
	user=serializers.IntegerField()
	address = serializers.CharField(max_length=100)
	phone = serializers.CharField(max_length=24)


	class Meta:
		model = Users_extended
		fields = ('user','username','email','address','phone')

	def save(self):
		email=self.validated_data['email']
		username=self.validated_data['username']
		user=self.validated_data['user']
		address=self.validated_data['address']
		phone=self.validated_data['phone']
			#if your username is existing get the query of your specific username 
		userd=User.objects.get(id=user)
		userds = Users_extended.objects.get(user=user)
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
		if User.objects.filter(email=email).exists() :
			send_mail(
            'rest password', 
            'this is code : {}'.format(number), 
            'youssefouah1997@gmail.com', 
                [
                email, 
                ]
            ) 
			code[email] = number
			id = User.objects.get(email=email).id
		else :
			return Response(status=status.HTTP_404_NOT_FOUND)	
		
		return Response(data = str(id),status=status.HTTP_200_OK)

class rest_serializer_2(serializers.ModelSerializer):
	code=serializers.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['code']
		
	def validation(self):
		code_entry=self.validated_data['code']
		email = User.objects.get(id=4).email
		if int(code_entry) == int(code[email]):
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

class rest_serializer_3(serializers.ModelSerializer):
	new_password=serializers.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['new_password']
		
	def change(self):
		new_password=self.validated_data['new_password']
		user=User.objects.get(id=4)
		user.set_password(new_password)
		user.save()
		del code[User.objects.get(id=id).email]
		return Response(status=status.HTTP_200_OK)

#table scocial_links:
class Sociallinkserialiser(serializers.ModelSerializer):
	user_id=serializers.CharField(max_length=100)
	class Meta:
		model = social_profile
		fields = ['socialProfileUsername','user_id','urlOptionId','created_at','updated_at']
	
	def save(self):
		userid =self.validated_data['user_id']
		user = User.objects.get(username=userid)
		data = social_profile(socialProfileUsername = self.validated_data['socialProfileUsername'],
		userurl_id = user,urlOptionId = self.validated_data['urlOptionId'],
		created_at = self.validated_data['created_at'],updated_at = self.validated_data['updated_at'])	
		data.save()
		print(data)
		return data

class UpdateSocialserialiser(serializers.ModelSerializer):
	user_id=serializers.CharField(max_length=100)
	id = serializers.CharField(max_length=100)
	class Meta:
		model = social_profile
		fields = ['id','socialProfileUsername','user_id','urlOptionId','created_at','updated_at']
	
	def update(self):

		id_url =self.validated_data['id']
		print(id_url)
		userid =self.validated_data['user_id']
		user = User.objects.get(username=userid)
		print(user)
		socialprofileusername =self.validated_data['socialProfileUsername']
		urloptionid =self.validated_data['urlOptionId']
		created_at = self.validated_data['created_at']
		updated_at = self.validated_data['updated_at']

		if social_profile.objects.filter(id=id_url).exists():
			data = social_profile.objects.get(id=id_url)
			data.socialProfileUsername = socialprofileusername
			data.userurl_id = user
			data.urlOptionId = urloptionid
			data.created_at = created_at
			data.updated_at = updated_at
			data.save()
			return Response(status=status.HTTP_200_OK)	
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)


	    		



	
