from os import link
from django.contrib import admin
from .models import *


class Users_extendAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','user_id', 'phone', 'address','image','created_At','updated_At']

class Social_optionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','url_web','color_log','log_svg','log_svg_url']

class Social_urlAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','user_id','social_id','username','created_At','updated_At']




# Register your models here.
admin.site.register(Users_extend, Users_extendAdmin)
admin.site.register(social_option_name, Social_optionAdmin)
admin.site.register(social_url, Social_urlAdmin)