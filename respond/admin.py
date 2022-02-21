from os import link
from django.contrib import admin
from .models import Users,Links,Images

# Register your models here.
admin.site.register(Users)
admin.site.register(Links)
admin.site.register(Images)
