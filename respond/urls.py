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
     #path('rest_password_code/<int:id>/',views.rest_password_code,name = "rest_password_code"),
     path('rest_password/',views.rest_password,name = "rest_password"),
     path('add_social_profiles/',views.addsocial_links,name = "add_social"),
     path('get_user/no_url_profiles/<str:token>',views.get_user,name = "get_data_user"),
     path('get_user/url_profiles/<str:token>',views.get_urls_profile,name = "get_data_urls"),
     path('get_user_url_profile/<str:token>',views.get_user_url_profile,name = "get_data-user_and_urls"),
     path('update_url_profile/',views.updatesocial_links,name = "update_social"),
     path('social_links_options/',views.get_urls_option,name = "get_all_social_links"),
     path('delete_user_url_profile/<str:id>',views.delete_user_url_profile,name = "delete_user_url_profile"),
     path('upload_user_profile_picture',views.upload_user_profile_picture,name = "upload_user_profile_picture"),
     path('get_user_profile_picture/<str:token>',views.get_user_profile_picture,name = "uget_user_profile_picture"),
]