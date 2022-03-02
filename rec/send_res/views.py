from django.shortcuts import render
from .models import users
# Create your views here.






def respond(request):
    data = users.objects.get(id = 2)
    print(data.links)
    return render(request,"responder/index.html",{'data':data})