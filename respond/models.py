from distutils.command.upload import upload
from email.policy import default
import numbers
import uuid
#from turtle import update
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


#table for user
class Users_extended(models.Model):
    id = models.UUIDField(primary_key=True,auto_created=True,default=uuid.uuid4,editable=False)
    user_id= models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    phone = models.CharField(max_length = 24,null = True,blank = True,unique=True)
    address = models.CharField(max_length = 100,null = True,blank = True)
    job = models.CharField(max_length = 100,null = True,blank = True)
    #image = models.ImageField(upload_to = 'photos',null = True,blank = True)
    created_At = models.DateTimeField(auto_now_add=True, editable=False)
    updated_At = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return str(self.job)

#table for urls every user has
class urlOption(models.Model):

    id = models.UUIDField(primary_key=True,auto_created=True,default=uuid.uuid4, editable=False)
    urlOptionName = models.CharField(max_length=100)
    urlOptionUrl = models.URLField(blank = True)
    urlOptionColor = models.CharField(max_length=100,null = True,blank = True)
    svg_logo = models.FileField(upload_to = 'logos',null = True,blank = True)
    logo_url = models.CharField(max_length=100,null = True,blank = True)

    def __str__(self):
        return str(self.id)

#ids for users  and urls
class social_profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #id = models.autuui(primary_key=True)
    userurl_id = models.ForeignKey(User,on_delete=models.CASCADE)
    urlOptionId = models.ForeignKey(urlOption,on_delete=models.CASCADE,null = True)
    socialProfileUsername = models.CharField(max_length = 15,blank=True,null=True)
    created_At = models.DateTimeField(auto_now_add=True, editable=False)
    updated_At = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users_extended.objects.create(user_id=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.users_extended.save()    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)




