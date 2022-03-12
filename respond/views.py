from django.shortcuts import render

from .serializers import UsersSerialiser
from .models import Users
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,filters
# Create your views here.
from .serializers import RegistrationSerializer
from knox.models import AuthToken
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView




def respond(request,board_id):
    data = User.objects.get(username = board_id)
    print(data.users.phone)
    return render(request,"responder/index.html",{'data':data})


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UsersSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)   
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)    



@api_view(['GET', 'PUT', 'DELETE'])
@login_required(login_url='login')
def upd_add_del(request,board_id):
    try:
        data_user = User.objects.get(username = board_id)
        data = data_user.users
    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     

    if request.method == 'GET':
        ser = UsersSerialiser(data)
        return Response(ser.data)   

    if request.method == 'PUT':
        ser = UsersSerialiser(data,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)   

    if request.method == 'DELETE':
        data.delete()   
    return Response(ser.data,status=status.HTTP_204_NO_CONTENT)        


@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = AuthToken.objects.create(account)[1]
			data['email'] = account.email
			data['username'] = account.username
		else:
			data = serializer.errors
		return Response(data)



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



