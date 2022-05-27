from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token




def respond(request,board_id):
    data = User.objects.get(username = board_id)
    print(data.users.extended.phone)
    return render(request,"responder/index.html",{'data':data})


# this function for GRUD profile
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated,])
def edit_profile(request,id):
    try:
        #getting data this id
        id_hash = Users_extended.objects.get(id=id).user_id
        data_user = User.objects.get(username = id_hash)
        data = data_user.users_extended

    except :
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
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)     

    #delete data in table users
    if request.method == 'DELETE':
        data_user.delete()  
        data.delete() 
    return Response(status=status.HTTP_304_NOT_MODIFIED)      


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            #data['response'] = message["user registered successfully"]
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
           #data = message["the username or the email is already exist"]
           return Response(status=status.HTTP_208_ALREADY_REPORTED)
        return Response(data,status=status.HTTP_201_CREATED)


#this function for login
#return {"token":token,"username":username,"email":email,"id":id,}
@api_view(['POST', ])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        datas = {}
        datas_urls = {}
        if serializer.is_valid():

            try:
                #check if input is username or email 
                if '@' in serializer.data['username']:
                    email = User.objects.get(email=serializer.data['username'])
                    username =email
                    data = email.users_extended
                    #userdata_urls.objects.filter(userurl_id = username).all()
                    user = authenticate(username=username, password=serializer.data['password'])
                else:
                    #in I replace variable username by a variable email
                    email = User.objects.get(username=serializer.data['username']) 
                    data = email.users_extended
                    print(email)
                    userdata_urls = social_profile.objects.filter(userurl_id = email)
                    print(userdata_urls.values('userurl_id').all())
                    for q in userdata_urls:
                        for key, value in q.items():
                            datas[key] = value
                    print(datas)
                    #userdata_urles = userdata_urls.objects.filter(userurl_id = username)
                    user = authenticate(username=email, password=serializer.data['password'])

            except:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
       
            if user == None:
                 return Response(status=status.HTTP_404_NOT_FOUND)

            else:
                 token = Token.objects.get(user_id= email.id).key
                 datas['token'] = token
                 datas['email'] = email.email
                 datas['username'] = email.username
                 datas['id'] = data.id
                 datas['job'] = data.job
                 datas['phone'] = data.phone
                 datas['address'] = data.address
                 datas['created_at'] = data.created_At
                 datas['updated_at'] = data.updated_At


                 return Response(datas,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)                 



#this function for forgot password :give username and old password and new password
@api_view(['PUT', ])
def change_password(request):

    if request.method == 'PUT':
        serializer=forgot_rest_serializer(data=request.data)

    if serializer.is_valid():
        msg = serializer.save()
        return msg

    return Response(status=status.HTTP_204_NO_CONTENT)

#this function for sending email to user givin email
@api_view(['POST', ])
def rest_password_email(request):
    if request.method == 'POST':
        serializer = rest_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            id = serializer.sending()
            return Response(data = str(id),status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


#this function for get is code verfied or not
@api_view(['POST', ])
def rest_password_code(request,id):
    if request.method == 'POST':
        serializer = rest_serializer_2(data=request.data)
        if serializer.is_valid():
            code = serializer.validation()
            return Response(data=code)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)    

#this function for rest password
@api_view(['POST', ])
def rest_password(request,id):
    if request.method == 'POST':
        serializer = rest_serializer_3(data=request.data)
        if serializer.is_valid():
            code = serializer.change(id)
            return Response(code)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)    
        
            


@api_view(['PUT','GET' ])
def addsocial_links(request,id):
    try:
        data = urlOption.objects.get(id = id)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serializer=Sociallinkserialiser(data)
        return Response(serializer.data,status=status.HTTP_200_OK)



    if request.method == 'PUT':
        serializer=Sociallinkserialiser(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_Modified_204)

    #delete data in table links
    if request.method == 'DELETE':
        data.delete()   


    return Response(status=status.HTTP_417_EXPECTATION_FAILED)


#table social_option
@api_view(['GET', ])
def getsocial_links(request):

    try:
        data = social_profile.objects.all()
    except:
        return Response(status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer=Social_links_options(data)
        return Response(serializer.data)

    return Response(status=status.HTTP_417_EXPECTATION_FAILED)






































#class LoginAPI(KnoxLoginView):
 #   permission_classes = (permissions.AllowAny,)
  #  def post(self, request, format=None):
   #     serializer = AuthTokenSerializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
     #   user = serializer.validated_data['user']
      #  login(request, user)
       # return super(LoginAPI, self).post(request, format=None)

