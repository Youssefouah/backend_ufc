from email import header
from django.urls import path
from . import views
from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     # root path
     path('page_main_view/<str:board_id>/',views.respond,name = 'repond'),
     # auth paths
     path('signup/',views.registration_view), 
     path('login/',views.login_in,name = "login"), 
     path('logout/',views.logout_out,name = "logout"), 
     # security paths
     path('change_password/',views.change_password,name = "forgot_password"),
     path('rest_password_by_email/',views.rest_password_email,name = "rest_password_email"),
     #path('rest_password_code/<int:id>/',views.rest_password_code,name = "rest_password_code"),
     path('rest_password/',views.rest_password,name = "rest_password"),
     # add data paths
     path('add_user_social_profile/',views.addsocial_links,name = "add_social"),
     path('upload_user_profile_picture/',views.upload_user_profile_picture,name = "upload_user_profile_picture"),
     # update data paths
     path('edit_profile/',views.edit_profile),
     path('update_url_profile/token:<str:token>',views.updatesocial_links,name = "update_social"),
     # get data paths
     path('get_bare_user/',views.get_user,name = "get_data_user"),
     path('get_full_user/',views.get_full_user,name = "get_data-user_and_urls"),
     path('get_user_profile_picture/',views.get_user_profile_picture,name = "uget_user_profile_picture"),
     path('get_user/single_url_profile/',views.get_urls_profile,name = "get_data_urls"),
     path('get_social_profile/username:<str:username>',views.get_social_profile,name = "get_data_urls"),
     path('get_user_social_urls/',views.get_user_social_urls,name = "get_data_urls"),
     path('get_link_options/',views.get_link_options,name = "get_all_link_options"),
     # delete data paths
     path('delete_user_social_profiles/<str:id>',views.delete_user_url_profile,name = "delete_user_url_profile"),
]