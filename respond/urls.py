from django.urls import path
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('recs/<str:board_id>/',views.respond,name = 'repond'),
     #path('post',views.create_user), 
     path('post/<str:board_id>/',views.upd_add_del),
     path('log',views.registration_view), 
     path('login',obtain_auth_token,name = "login"), 
]