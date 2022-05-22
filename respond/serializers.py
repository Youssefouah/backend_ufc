from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User



class UsersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PutusersSerialiser(serializers.ModelSerializer):
	username=serializers.CharField(max_length=100)
	email=serializers.CharField(max_length=100)
	user=serializers.IntegerField()
	address = serializers.CharField(max_length=100)
	phone = serializers.CharField(max_length=24)


	class Meta:
		model = Users
		fields = ('user','username','email','address','phone')

	def save(self):
		email=self.validated_data['email']
		username=self.validated_data['username']
		user=self.validated_data['user']
		address=self.validated_data['address']
		phone=self.validated_data['phone']
			#if your username is existing get the query of your specific username 
		userd=User.objects.get(id=user)
		userds = Users.objects.get(user=user)
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

	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'password2']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = User(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
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
	password=serializers.CharField(max_length=100)

	class Meta:
		model = User
		fields = '__all__'

	def save(self):
		password=self.validated_data['password']
		username=self.validated_data['username']

		 #filtering out whethere username is existing or not, if your username is existing then if condition will allow your username
		if User.objects.filter(username=username).exists():

			#if your username is existing get the query of your specific username 
			user=User.objects.get(username=username)

			#then set the new password for your username
			user.set_password(password)
			user.save()
			return user
		else:
			raise serializers.ValidationError({'error':'please enter valid crendentials'})	




