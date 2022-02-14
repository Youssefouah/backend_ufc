from django.urls import path
from . import views


urlpatterns = [
    path('recs',views.respond,name = 'repond'),
]