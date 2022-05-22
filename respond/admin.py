from os import link
from django.contrib import admin
from .models import Users_extend,Social_option,Social_url

# Register your models here.
admin.site.register(Users_extend)
admin.site.register(Social_option)
admin.site.register(Social_url)