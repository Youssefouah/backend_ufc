from django.urls import path
from . import views


urlpatterns = [
    path('res',views.responder,name = 'reponder'),
]