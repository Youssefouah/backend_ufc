from django.shortcuts import render
from django.http import JsonResponse
from .models import users
import requests
# Create your views here.






def respond(request,board_id):
    data = users.objects.get(id = board_id)
    print(data.links)
    return render(request,"responder/index.html",{'data':data})


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

def sending(request) :
    data = {
          'name' : 'mahboub mohmmed',
          'gmail' : 'mahboub_mohmmed@gamil.com',
          'phone' : '056236424',
          'password' : '0000',
          'image':'user1.jpg',

          'links':{"facebook ": "www.facbook.com", 
          "twitter ": "www.twitter.com", 
          "google": "www.google.com", 
          "skype ": "www.skype.com", "yahoo": "www.yahoo.com", "snapchat-ghost": "www.snapchat-ghost.com"}

    }  
    return JsonResponse(data)