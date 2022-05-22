from django.urls import path
from . import views
from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('page_main_view/<str:board_id>/',views.respond,name = 'repond'),
     #path('post',views.create_user), 
     path('edit_profile/<int:id>/',views.edit_profile),
     path('Sign_up/',views.registration_view), 
     path('login/',views.login,name = "login"), 
     path('forgot_password/',views.rest_password,name = "forgot_password"),
]