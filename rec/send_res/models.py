
from distutils.command.upload import upload
from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User,AbstractUser


# Create your models here.


class User(AbstractUser):
    gmail = models.EmailField(unique=True)
    phone = models.CharField(max_length = 24,unique =True,null = True,blank = True)
    image = models.ImageField(upload_to = 'photos',default = 'user1.jpeg',null = True,blank = True)
    links = models.JSONField(null = True)





class users(models.Model):
    name = models.CharField(max_length=15)
    gmail = models.CharField(max_length=44)
    phone = models.CharField(max_length=15,null = True,blank = True)
    password = models.CharField(max_length=15)
    active = models.BooleanField(default= False)
    image = models.ImageField(upload_to = 'photos',default = 'user1.jpeg')
    links = models.JSONField(null = True)

    def __str__(self):
        return self.name