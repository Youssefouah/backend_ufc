from django.shortcuts import render

# Create your views here.
from .models import Users,Links,Images
# Create your views here.

def classifcation(list1,list2):
    l = []
    for i in range(len(list1)):
        ll = []
        ll.append(list1[i])
        ll.append(list2[i])
        l.append(ll)

    return l

def responder(request):
    data = Users.objects.get(id=1)
    link = data.link.__dict__
    images = data.images.__dict__

    del link["_state"]
    del link["id"]
    del images["_state"]
    del images["id"] 

    datas = classifcation(list(link.values()),list(images.values()))
                    
    return render(request,"responder/index.html",{'data':data,"links":datas})


