from django.urls import path
from . import views


urlpatterns = [
    path('recs/<int:board_id>/',views.respond,name = 'repond'),
    path('sending',views.sending,name = 'send_data'),
    path('stock',views.stock,name = 'stock_data'),
]