from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'send_res/',views.userviews, basename='MyModel')


urlpatterns = [
    path('recs/<int:board_id>/',views.respond,name = 'repond'),
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login'),
    path('sending',views.sending,name = 'send_data'),
    path('add',views.add,name = 'add'),
    path('logout',views.logout,name = 'logout'),
    path('stock',views.stock,name = 'stock_data'),
    path('stik',include(router.urls)),
]