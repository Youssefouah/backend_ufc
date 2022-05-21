from dataclasses import field
from httplib2 import Authentication
from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User



class UsersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = 'name','phone','image','links'

        

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

	class Meta:
		model = User
		fields = ['email', 'password']	
