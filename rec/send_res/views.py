from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import users
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.
from rest_framework import viewsets
from .serializers import UsersSerialiser



class userviews(viewsets.ModelViewSet):
    queryset = data = users.objects.all() 
    serializer_class = UsersSerialiser 




def respond(request,board_id):
    data = users.objects.get(id = board_id)
    print(data.links)
    return render(request,"responder/index.html",{'data':data})
  

def register(request):
    response = requests.get("http://127.0.0.1:8000/res/sending")
    content = response.json()
    if (users.objects.get(gmail = content['gmail'])) == None:
        data =  users()
        data.name = content['name']
        data.gmail= content['gmail']
        data.password = content['password']   
        data.save()
    else : 
        return redirect('send_data')        


def login(request):
    response = requests.get("http://127.0.0.1:8000/res/sending")
    content = response.json()
    data = users.objects.get(gmail = content['gmail'])
    if data != None and data.password == content['password'] and data.gmail == content['gmail'] and data.active == False:
       data.active = True
       data.save()
       return redirect('/')


def add(request):
    response = requests.get("http://127.0.0.1:8000/res/sending")
    content = response.json()    
    data = users.objects.get(gmail = content['gmail'])
    if data.active == True:
        data.phone = content['phone']
        data.image = content['image']
        data.links = content['links'] 
        data.save()
        return redirect('/')    


def logout(request):
    response = requests.get("http://127.0.0.1:8000/res/sending")
    content = response.json()    
    data = users.objects.get(gmail = content['gmail'])   
    if data.active == True: 
        data.active = False  
        print('sucess')         
        return redirect('/send_data')  
    else : 
        print('sucess') 
        return redirect('/')      

def stock(request):
    response = requests.get("http://127.0.0.1:8000/res/sending")
    content = response.json()
    data =  users()
    data.name = content['name']
    data.gmail= content['gmail']
    data.phone = content['phone']
    data.image = content['image']
    data.password = content['password']
    data.links = content['links']
    data.save()
    print(content)
    return JsonResponse(content)





@csrf_exempt
def sending(request) :
    data = {
          'name' : 'mahboub ',
          'gmail' : 'mahboub@gamil.com',
          'phone' : '05623456424',
          'password' : '000045',
          'image':'photos/user1.jpg',
           
          'links':{"facebook ": "www.facbook.com", 
          "twitter ": "www.twitter.com", 
          "google": "www.google.com", 
          "skype ": "www.skype.com", "yahoo": "www.yahoo.com", "snapchat-ghost": "www.snapchat-ghost.com"}

    } 
    name =  request.POST.get('name')
    print(name)
    return JsonResponse(data)