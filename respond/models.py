from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null = True,unique=True)
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length = 24,null = True,blank = True)
    image = models.ImageField(upload_to = 'photos',null = True,blank = True)
    links = models.JSONField(null = True)
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.users.save()    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)






