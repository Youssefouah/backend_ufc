from os import link
from django.contrib import admin
from .models import Users_extend,Social_option,Social_url


class Users_extendAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['user', 'phone', 'address','image','new_created','time_close']

class Social_optionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['url_web','color_log','log_svg']

class Social_urlAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['user_id','social_id','username_id','url_socials','new_created','new_update','numbers_clicks']




# Register your models here.
admin.site.register(Users_extend, Users_extendAdmin)
admin.site.register(Social_option, Social_optionAdmin)
admin.site.register(Social_url, Social_urlAdmin)