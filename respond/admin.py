from os import link
from django.contrib import admin
from .models import *


class Users_extendAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','user_id','job','address','phone','created_At','updated_At']

class Social_optionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','urlOptionName','urlOptionUrl','urlOptionColor','svg_logo','logo_url']

class Social_urlAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','userurl_id','urlOptionId','socialProfileUsername','created_At','updated_At']




# Register your models here.
admin.site.register(Users_extended, Users_extendAdmin)
admin.site.register(urlOption, Social_optionAdmin)
admin.site.register(social_profile, Social_urlAdmin)

# Register your models here.
