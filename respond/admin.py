from os import link
from django.contrib import admin
from .models import *


class Users_extendAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','user_id','job','address','image','phone','created_At','updated_At']

class Social_optionAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','urlOptionName','urlOptionUrl','urlOptionColor','svg_logo','logo_url','hint']

class Social_urlAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','userurl_id','urlOptionId','socialProfileUsername','created_at','updated_at']

class Table_statusAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id','user_id','url_id','number_of_times_visited','number_of_times_shared','number_of_times_clicked']



# Register your models here.
admin.site.register(Users_extended, Users_extendAdmin)
admin.site.register(urlOption, Social_optionAdmin)
admin.site.register(social_profile, Social_urlAdmin)
admin.site.register(stats_table, Table_statusAdmin)

# Register your models here.
