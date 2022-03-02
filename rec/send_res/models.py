from datetime import timezone
from distutils.command.upload import upload
from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.



class users(models.Model):
    name = models.CharField(max_length=15)
    gmail = models.CharField(max_length=44)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    image = models.ImageField(upload_to = 'photos',default = 'user1.jpeg')
    links = models.JSONField(null = True)

    def __str__(self):
        return self.name