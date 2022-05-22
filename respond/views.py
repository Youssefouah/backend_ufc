from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import authenticate
from yaml import serialize
from .serializers import UsersSerialiser,LoginSerializer,forgot_rest_serializer,UserSerialiser,PutusersSerialiser
from .models import Users
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,filters
# Create your views here.
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password


def respond(request,board_id):
    data = User.objects.get(username = board_id)
    print(data.users.phone)
    return render(request,"responder/index.html",{'data':data})


#@api_view(['POST'])
#def create_user(request):
 #   if request.method == 'POST':
  #      serializer = UsersSerialiser(data=request.data)
   #     if serializer.is_valid():
    #        serializer.save()
     #   return Response(serializer.data,status=status.HTTP_201_CREATED)   
    #return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)    



@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated,])
def edit_profile(request,id):
    datas = {}
    try:
        data_user = User.objects.get(id = id)
        data = data_user.users

    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)     

    if request.method == 'GET':
        ser = UsersSerialiser(data)
        ser1 = UserSerialiser(data_user)

        #data in table users
        table_users = dict(ser.data)

        #data_user in table user
        table_user = dict(ser1.data)

        #all data for user
        table_all = table_users|table_user
        return Response(table_all)   
    
    #edit data in table users("image ,adress,phone")
    if request.method == 'PUT':
        serlizer = PutusersSerialiser(data,data=request.data)

        if serlizer.is_valid(raise_exception=True):
            serlizer.save()
            datas["message"] = "edit data in table users"
            return Response(datas,status=status.HTTP_201_CREATED)

        return Response(serlizer.errors,status=status.HTTP_400_BAD_REQUEST)     

    #delete data in table users
    if request.method == 'DELETE':
        data.delete()   
    return Response(ser1.data,status=status.HTTP_204_NO_CONTENT)        


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Token.objects.create(account)."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    
@api_view(['POST', ])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        datas = {}
        if serializer.is_valid():

            try:
                #check if input is username or email 
                if '@' in serializer.data['username']:
                    email = User.objects.get(email=serializer.data['username'])
                    username =email
                    user = authenticate(username=username, password=serializer.data['password'])
                else:
                    #in I replace variable username by a variable email
                    email = User.objects.get(username=serializer.data['username']) 
                    user = authenticate(username=email, password=serializer.data['password'])

            except:
                datas['response'] = "the username or password is incorrect"
                return Response(datas,status=status.HTTP_404_NOT_FOUND)
       
            if user == None:
                 datas['response'] = "the username is not exist"
                 return Response(datas,status=status.HTTP_400_BAD_REQUEST)

            else:
                 token = Token.objects.get(user_id= email.id).key
                 datas['token'] = token
                 datas['email'] = email.email
                 datas['username'] = email.username
                 datas['user_id'] = str(email.id)
            
                 return Response(datas,status=status.HTTP_200_OK)
        else:
            datas['response'] = "the username or password is not correct.please try again"
            return Response(datas,status=status.HTTP_400_BAD_REQUEST)                 




@api_view(['POST', ])
def rest_password(request):

    if request.method == 'POST':
        serializer=forgot_rest_serializer(data=request.data)
        datas={}

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        datas['data']='successfully registered'
        print(datas)
        return Response(datas)

    return Response('failed retry after some time')































#class LoginAPI(KnoxLoginView):
 #   permission_classes = (permissions.AllowAny,)
  #  def post(self, request, format=None):
   #     serializer = AuthTokenSerializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
     #   user = serializer.validated_data['user']
      #  login(request, user)
       # return super(LoginAPI, self).post(request, format=None)

"""

            token = Token.objects.get(user_id= data.id).key
            datas['token'] = token
            datas['email'] = email
            datas['username'] = username
            datas['user_id'] = str(data.id)
            return Response(data,status=status.HTTP_200_OK)
"""

