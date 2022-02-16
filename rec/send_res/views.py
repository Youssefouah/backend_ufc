from django.shortcuts import render
from .models import users,links
# Create your views here.


def respond(request):
    data = users.objects.get(name = 'dakir')
    link = links.objects.all()
    return render(request,"responder/index.html",{'data':data,'links':link})