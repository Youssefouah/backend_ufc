from os import link
from django.contrib import admin
from .models import Users,Social_options,Social_urls

# Register your models here.
admin.site.register(Users)
admin.site.register(Social_options)
admin.site.register(Social_urls)