from django.urls import path
from . import views
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path

urlpatterns = [
     path('recs/<str:board_id>/',views.respond,name = 'repond'),
     path('post',views.create_user), 
     path('mod/<str:board_id>/',views.upd_add_del),
     path('log',views.registration_view), 
     path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]