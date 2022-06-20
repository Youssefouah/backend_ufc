import base64
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
from django.core.files.base import ContentFile


#code = {}



class Urlsserialiser(serializers.ModelSerializer):
	class Meta:
		model = social_profile
		fields = '__all__'


class urlsOpseriamiser(serializers.ModelSerializer):
	class Meta:
		model = urlOption
		fields = '__all__'		



class UsersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users_extended
        fields = ('id','job','address','phone','created_At','updated_At')

class PutusersSerialiser(serializers.ModelSerializer):
	username=serializers.CharField(max_length=100)
	email=serializers.CharField(max_length=100)
	#user=serializers.IntegerField()
	address = serializers.CharField(max_length=100)
	phone = serializers.CharField(max_length=30)
	job = serializers.CharField(max_length=100)
	token = serializers.CharField(max_length=100)
	id = serializers.UUIDField()
	class Meta:
		model = Users_extended
		fields = ('username','email','address','phone','job','token','id')

	def save(self):
		email=self.validated_data['email']
		username=self.validated_data['username']
		#user=self.validated_data['user']
		address=self.validated_data['address']
		phone=self.validated_data['phone']
		job=self.validated_data['job']
		token=self.validated_data['token']
		id=self.validated_data['id']
			#if your username is existing get the query of your specific username 
		userds = Users_extended.objects.get(id=id)
		userd=User.objects.get(username=userds.user_id.username)
		#data_tocken = Token.objects.get(user_id=userd.id)
			#then set the new username and email to the existing username
		userd.username=username
		userd.email=email

			#then set the new address and phone to the existing address and phone
		userds.address=address
		userds.phone=phone	
		userds.job=job


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
						return Response(status=status.HTTP_401_UNAUTHORIZED)
				else:
					return Response(status=status.HTTP_404_NOT_FOUND)		
			except:
				return Response(status=status.HTTP_502_BAD_GATEWAY)			

	
		elif User.objects.filter(username=username).exists() :
			#print(username)
			if authenticate(username=username, password= old_password):
				user=User.objects.get(username=username)
				user.set_password(new_password)
				user.save()
				return Response(status=status.HTTP_200_OK)
			else :
				return Response(status=status.HTTP_401_UNAUTHORIZED)	

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
			#code[email] = number
		else :
			return Response(status=status.HTTP_404_NOT_FOUND)	
		
		return str(number)

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
	email = serializers.CharField(max_length=100)	
	new_password=serializers.CharField(max_length=100)
	class Meta:
		model = User
		fields = ['new_password','email']
		
	def change(self):
		#print(code)	
		email = self.validated_data['email']
		new_password=self.validated_data['new_password']
		user = User.objects.get(email=email)
		print(user)
		user.set_password(new_password)
		user.save()
		#del code[User.objects.get(email=email).email]
		return Response(status=status.HTTP_200_OK)

#table scocial_links:
class Sociallinkserialiser(serializers.ModelSerializer):
	username=serializers.CharField(max_length=100)
	class Meta:
		model = social_profile
		fields = ['socialProfileUsername','username','urlOptionId']
	
	def save(self):
		userid =self.validated_data['username']
		user = User.objects.get(username=userid)
		data = social_profile(socialProfileUsername = self.validated_data['socialProfileUsername'],
		userurl_id = user,urlOptionId = self.validated_data['urlOptionId'])	
		data.save()
		return data

class UpdateSocialserialiser(serializers.ModelSerializer):
	user_id=serializers.CharField(max_length=100)
	id = serializers.CharField(max_length=100)
	socialProfileUsername = serializers.CharField(max_length=100)
	urlOptionId = serializers.CharField(max_length=100)
	class Meta:
		model = social_profile
		fields = ['id','socialProfileUsername','user_id','urlOptionId']
	
	def update(self):

		id_url =self.validated_data['id']
		print(id_url)
		userid =self.validated_data['user_id']
		user = User.objects.get(username=userid)
		print(user)
		socialprofileusername =self.validated_data['socialProfileUsername']
		urloptionid =self.validated_data['urlOptionId']
		#created_at = self.validated_data['created_at']
		#updated_at = self.validated_data['updated_at']

		if social_profile.objects.filter(id=id_url).exists():
			data = social_profile.objects.get(id=id_url)
			urloptionid_url =  urlOption.objects.get(id=urloptionid)
			data.socialProfileUsername = socialprofileusername
			data.userurl_id = user
			data.urlOptionId = urloptionid_url
		#	data.created_at = created_at
		#	data.updated_at = updated_at
			data.save()
			return Response(status=status.HTTP_200_OK)	
		else:
			return Response(status=status.HTTP_404_NOT_FOUND)

class ProfilePictureSerializer(serializers.ModelSerializer):
	#id=serializers.CharField(max_length=100)
	image = serializers.ImageField(max_length=None, use_url=True)
	class Meta:
		model = Users_extended
		fields = ['image']
	
	def save(self,userid):
		#userid =self.validated_data['id']
		image = self.validated_data['image']
		user = Users_extended.objects.get(id=userid)
		your_file = ContentFile(base64.b64decode(image))
		if user.image:
			user.image.delete()	
		user.image = your_file
		user.save()
		return Response(status=status.HTTP_200_OK)
	    		



	
