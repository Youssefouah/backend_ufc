from django.urls import path
from . import views
from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('page_main_view/<str:board_id>/',views.respond,name = 'repond'),
     #path('post',views.create_user), 
     path('edit_profile/<str:id>/',views.edit_profile),
     path('signup/',views.registration_view), 
     path('login/',views.login,name = "login"), 
     path('change_password/',views.change_password,name = "forgot_password"),
     path('rest_password_email/',views.rest_password_email,name = "rest_password_email"),
     path('rest_password_code/<int:id>/',views.rest_password_code,name = "rest_password_code"),
     path('rest_password/<int:id>/',views.rest_password,name = "rest_password"),
     path('add_social_links/',views.addsocial_links,name = "add_social"),
     path('update_social_links/',views.updatesocial_links,name = "update_social"),
]