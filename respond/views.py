from email import message
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication



def get_user_by_token(id):
    try:
        id_hash = Users_extended.objects.get(id=id).user_id
        data_user = User.objects.get(username = id_hash)
        data = data_user.users_extended
        token = Token.objects.get(user=data_user).key
        return True
    except:
        return False
#show in template 
def respond(request,board_id):
    id_hash = Users_extended.objects.get(id=board_id).user_id
    data = User.objects.get(username = id_hash)
    print(data.users_extended.phone)
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

def is_token_in_table(token):
    try:
        data = Token.objects.get(key=token)
        return True
    except:
        return False


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
@authentication_classes((TokenAuthentication,))
def edit_profile(request):
        datar = {}
        if request.user.is_authenticated:
            #getting data this id
            #id_hash = Users_extended.objects.get(id=id).user_id
            data_user = User.objects.get(username = request.user.username)
            data = data_user.users_extended
            token = Token.objects.get(user=data_user).key
            datar['token'] = token
        else :
            return Response(status=status.HTTP_401_UNAUTHORIZED)   
    

        if request.method == 'GET':
            table_all = get_datathe_user(data,data_user)
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
@authentication_classes((TokenAuthentication,))
def delete_user_url_profile(request):
        if request.user.is_authenticated:
            data_users = Users_extended.objects.get(user_id=request.user)
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
        else:
             Response(status=status.HTTP_401_UNAUTHORIZED)      



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
def login_in(request):
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
                    #datas_urls = get_social_profile(username) 
                    #userdata_urls.objects.filter(userurl_id = username).all()
                    user = authenticate(username=username, password=serializer.data['password'])
                else:
                    #in I replace variable username by a variable email
                    email = User.objects.get(username=serializer.data['username']) 
                    data = email.users_extended
                    #datas_urls = get_social_profile(email) 
                    #userdata_urles = userdata_urls.objects.filter(userurl_id = username)
                    user = authenticate(username=email, password=serializer.data['password'])

            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
       
            if user == None:
                 return Response(status=status.HTTP_401_UNAUTHORIZED)

            else:
                 login(request,user)
                 token = Token.objects.get(user_id= email.id).key
                 datas['token'] = token
                 datas['email'] = email.email
                 datas['username'] = email.username
                 datas['id'] = data.id
                 #datas['job'] = data.job
                 #datas['phone'] = data.phone
                 #datas['address'] = data.address
                 #datas['created_at'] = data.created_At
                 #datas['updated_at'] = data.updated_At
                # datas['url_profiles'] = datas_urls

                 return Response(datas,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)                 

def logout_out(request):
    logout(request)

#this function for forgot password :give username and old password and new password
@api_view(['PUT', ])
@authentication_classes((TokenAuthentication,))
def change_password(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'PUT':
            serializer=forgot_rest_serializer(data=request.data)

        if serializer.is_valid():
            msg = serializer.save()
            return msg

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status=status.HTTP_401_UNAUTHORIZED)    

#this function for sending email to user givin email
@api_view(['POST', ])
@authentication_classes((TokenAuthentication,))
def rest_password_email(request):
    if request.user.is_authenticated:
        serializer = rest_serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            id = serializer.sending()
            return Response(data = str(id),status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)        


#this function for get is code verfied or not
# @api_view(['POST', ])
# def rest_password_code(request,id):
#     if request.method == 'POST':
#         serializer = rest_serializer_2(data=request.data)
#         if serializer.is_valid():
#             code = serializer.validation()
#             return Response(data=code)
#         else:
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE)    

#this function for rest password
@api_view(['POST', ])
@authentication_classes((TokenAuthentication,))
def rest_password(request):
    if request.user.is_authenticated:
        serializer = rest_serializer_3(data=request.data)
        if serializer.is_valid():
            code = serializer.change()
            return code
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)   
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)         
        
            
"""
this function for add social profile
 {
    "urlOptionId": "2cef0a5f-3844-40fe-8f9f-dea132b32cb5",
    "socialProfileUsername": "youssef55",
    "user_id": "youssef",
  }
"""

@api_view(['POST' ])
@authentication_classes((TokenAuthentication,))
def addsocial_links(request):
        if request.user.is_authenticated:
            serialize=Sociallinkserialiser(data=request.data)
       # print(serialize)
            if serialize.is_valid() :
                serialize.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)      
   
@api_view(['PUT' ])
@authentication_classes((TokenAuthentication,))
def updatesocial_links(request):
       if request.user.is_authenticated:
            serialize=UpdateSocialserialiser(data=request.data)
        # print(serialize)
            if serialize.is_valid() :
                serialize.update()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_417_EXPECTATION_FAILED)
       else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)    


# this function is to get the user if authenticated 
@api_view(['GET' ])
@authentication_classes((TokenAuthentication,))
def get_user(request):
   
    if request.user.is_authenticated:
        user = request.user
        datas = User.objects.get(username=user)
        data = datas.users_extended
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        #all data for user
        table_all = get_datathe_user(data,datas)
        return Response(table_all,status = status.HTTP_200_OK)   
    return Response( status=status.HTTP_417_EXPECTATION_FAILED)

#return user with url
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_urls_profile(request):
    if request.user.is_authenticated:
        user = request.user
        datas = User.objects.get(username=user)
        data = get_social_profile(datas)
        return Response(data[0],status = status.HTTP_200_OK) 

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED) 
          

#return user with url
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_full_user(request):
    if request.user.is_authenticated:
        user = request.user
        datas = User.objects.get(username=user)
        token = Token.objects.get(user=user).key
        data = datas.users_extended
        #return table useer
        table_user = get_datathe_user(data,datas)
        table_user['token'] = token
        #return urls
        data_url = get_social_profile(datas)
        if data_url != None:
            table_user['url_profiles'] = data_url
        else:
            table_user['url_profiles'] = []    
        return Response(table_user,status = status.HTTP_200_OK) 
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED) 


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_link_options(request):
        data_all =[]
        if request.user.is_authenticated:
            data = urlOption.objects.all()
            for i in data:
                datas = {
                    'id':str(i.id),
                    'urlOptionName':str(i.urlOptionName),
                    'urlOptionUrl':str(i.urlOptionUrl),
                    'urlOptionColor':str(i.urlOptionColor),
                    'svg_logo':str(i.svg_logo),
                    'logo_url':str(i.logo_url)}   
                data_all.append(datas)
            return Response(data_all,status = status.HTTP_200_OK) 
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
  
  
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_user_social_urls(request):
        all_data =[]
        if request.user.is_authenticated:
            data = social_profile.objects.all()
            for i in data:
                datas = {
                    'id':str(i.id),
                    'userurl_id':str(i.userurl_id),
                    'urlOptionId':str(i.urlOptionId),
                    'socialProfileUsername':str(i.socialProfileUsername),
                    'created_at':str(i.created_at),
                    'updated_at':str(i.updated_at)}   
                all_data.append(datas)
       
            return Response(all_data,status = status.HTTP_200_OK) 
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
  
  
         
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def upload_user_profile_picture(request):
    if request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = ProfilePictureSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.save()
                return data
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_417_EXPECTATION_FAILED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)    



@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def get_user_profile_picture(request):
    if request.user.is_authenticated:
        user = request.user
        datas = User.objects.get(username=user)
        data = datas.users_extended

        return Response(data.image.url,status = status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



































#class LoginAPI(KnoxLoginView):
 #   permission_classes = (permissions.AllowAny,)
  #  def post(self, request, format=None):
   #     serializer = AuthTokenSerializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
     #   user = serializer.validated_data['user']
      #  login(request, user)
       # return super(LoginAPI, self).post(request, format=None)

