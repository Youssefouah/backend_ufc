from django.urls import path
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('page_main_view/<str:board_id>/',views.respond,name = 'repond'),
     #path('post',views.create_user), 
     path('upgrade/<str:board_id>/',views.upd_add_del),
     path('Sign_up/',views.registration_view), 
     path('login',views.login,name = "login"), 
]