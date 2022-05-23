from distutils.command.upload import upload
from email.policy import default
import numbers
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


#table for user
class Users_extend(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null = True,unique=True)
   # name = models.CharField(max_length=15)
    phone = models.CharField(max_length = 24,null = True,blank = True)
    address = models.CharField(max_length = 100,null = True,blank = True)
    image = models.ImageField(upload_to = 'photos',null = True,blank = True)
    new_created = models.DateTimeField(auto_now_add=True, editable=False)
    time_close = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return str(self.user)

#table for urls every user has
class Social_option(models.Model):
    url_web = models.URLField(blank = True)
    color_log = models.CharField(max_length=100,null = True,blank = True)
    log_svg = models.FileField(upload_to = 'logos',null = True,blank = True)
    def __str__(self):
        return str(self.url)

#ids for users  and urls
class Social_url(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,null = True,unique=True)
    social_id = models.OneToOneField(Social_option,on_delete=models.CASCADE,null = True)
    username_id = models.CharField(max_length = 15,blank=True,null=True)
    url = models.URLField()
    new_created = models.DateTimeField(auto_now_add=True, editable=False)
    new_update = models.DateTimeField(auto_now=True, editable=False)
    numbers_clicks = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.user_id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users_extend.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.users.save()    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)






