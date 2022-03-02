from os import link
from django.contrib import admin
from .models import users

# Register your models here.
admin.site.register(users)
