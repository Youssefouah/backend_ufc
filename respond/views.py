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

#function for return db inside social_profile    
def get_datathe_user(data,data_user):
        ser = UsersSerialiser(data)
        ser1 = UserSerialiser(data_user)

        #data in table users
        table_users = dict(ser.data)

        #data_user in table user
        table_user = dict(ser1.data)

        #all data for user
        table_all = table_users|table_user
        return table_all

def get_social_profile(name_data):
    datass = []
    n=0
    try:
        data = social_profile.objects.all().filter(userurl_id=name_data)
       # print(data)
        for i in data:
            datas = {}
            #print(i.id)
            datas['id'] = str(i.id)
            datas['urlOptionId'] = str(i.urlOptionId)
            
            datas['socialProfileUsername'] = str(i.socialProfileUsername)
            datas['user_id'] = str(i.userurl_id)
            data_url = urlOption.objects.all().filter(id=str(i.urlOptionId))
            for j in data_url:
                datas['urlOptionName'] = str(j.urlOptionName)
                datas['urlOptionUrl'] = str(j.urlOptionUrl)
                datas['urlOptionColor'] = str(j.urlOptionColor)
                datas['svg_logo'] = str(j.svg_logo)
                datas['logo_url'] = str(j.logo_url)
            datass.append(datas)
        return datass
    except:
        return None

# this function for GRUD profile
@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated,])
def edit_profile(request,id):
    datar = {}
    try:
        #getting data this id
        id_hash = Users_extended.objects.get(id=id).user_id
        data_user = User.objects.get(username = id_hash)
        data = data_user.users_extended
        token = Token.objects.get(user=data_user).key
        datar['token'] = token

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
        table_all = table_users|table_user|datar
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

#delete user
@api_view([ 'DELETE'])
def delete_user_url_profile(request,id):
    try:
        data_users = Users_extended.objects.get(id=id)
        id_hash = data_users.user_id
        data_user = User.objects.get(username = id_hash)
        token = Token.objects.get(user=data_user)
        data_profile = social_profile.objects.all().filter(userurl_id=id_hash)
        data_profile.delete()
        data_user.delete()
        token.delete()
        data_users.delete()
        #for i in data_profile:
          #  print(i.id) 
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)



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
                    datas_urls = get_social_profile(username) 
                    #userdata_urls.objects.filter(userurl_id = username).all()
                    user = authenticate(username=username, password=serializer.data['password'])
                else:
                    #in I replace variable username by a variable email
                    email = User.objects.get(username=serializer.data['username']) 
                    data = email.users_extended
                    datas_urls = get_social_profile(email) 
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
                 datas['url_profiles'] = datas_urls

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
def rest_password(request):
    if request.method == 'POST':
        serializer = rest_serializer_3(data=request.data)
        if serializer.is_valid():
            code = serializer.change()
            return code
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)    
        
            
"""
this function for add social profile
 {
    "urlOptionId": "2cef0a5f-3844-40fe-8f9f-dea132b32cb5",
    "socialProfileUsername": "youssef55",
    "user_id": "youssef",
  }
"""

@api_view(['POST' ])
def addsocial_links(request):

    if request.method == 'POST':
        serialize=Sociallinkserialiser(data=request.data)
       # print(serialize)
        if serialize.is_valid() :
            serialize.save()
            return Response(status=status.HTTP_200_OK)
    return Response( status=status.HTTP_417_EXPECTATION_FAILED)      

@api_view(['PUT' ])
def updatesocial_links(request):
        if request.method == 'PUT':
            serialize=UpdateSocialserialiser(data=request.data)
        # print(serialize)
            if serialize.is_valid() :
                serialize.update()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_417_EXPECTATION_FAILED)



@api_view(['GET' ])
def get_user(request,token):

    try:
        user = Token.objects.get(key=token).user
        datas = User.objects.get(username=user)
        data = datas.users_extended

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #all data for user
        table_all = get_datathe_user(data,datas)
        return Response(table_all,status = status.HTTP_200_OK)   
    return Response( status=status.HTTP_417_EXPECTATION_FAILED)

#return user with url
@api_view(['GET'])
def get_urls_profile(request,token):
    try:
        user = Token.objects.get(key=token).user
        datas = User.objects.get(username=user)
        data = get_social_profile(datas)
        return Response(data[0],status = status.HTTP_200_OK) 

    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 
          

#return user with url
@api_view(['GET'])
def get_user_url_profile(request,token):
    try:
        user = Token.objects.get(key=token).user
        datas = User.objects.get(username=user)
        data = datas.users_extended
        #return table useer
        table_user = get_datathe_user(data,datas)
        #return urls
        data_url = get_social_profile(datas)

        table_user['url_profiles'] = data_url[0]
        return Response(table_user,status = status.HTTP_200_OK) 
    except:
        return Response(status=status.HTTP_404_NOT_FOUND) 


@api_view(['GET'])
def get_urls_option(request):
    data_all =[]
    try:
        data = urlOption.objects.all()
        for i in data:
            datas = {
                'id':str(i.id),
                'urlOptionName':str(i.urlOptionName),
                'urlOptionUrl':str(i.urlOptionUrl),
                'urlOptionColor':str(i.urlOptionColor),
                'svg_logo':str(i.svg_logo),
                'logo_url':str(i.logo_url)

            }   
            data_all.append(datas)
        #ser = urlsOpseriamiser(data)
        return Response(data_all,status = status.HTTP_200_OK) 
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

  
  
         
@api_view(['PUT'])
def upload_user_profile_picture(request):
    if request.method == 'PUT':
        serializer = ProfilePictureSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return data
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_417_EXPECTATION_FAILED)






"""
    #delete data in table links
    if request.method == 'DELETE':
        for i in data:
            i.delete()  
"""
"""
    try:
        id_hash = Users_extended.objects.get(id=id).user_id
        print(id_hash)
        data = urlOption.objects.all.filter(userurl_id = id_hash)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
"""



































#class LoginAPI(KnoxLoginView):
 #   permission_classes = (permissions.AllowAny,)
  #  def post(self, request, format=None):
   #     serializer = AuthTokenSerializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
     #   user = serializer.validated_data['user']
      #  login(request, user)
       # return super(LoginAPI, self).post(request, format=None)

