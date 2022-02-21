from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Links(models.Model):
    link1 = models.CharField(max_length=150)
    link2 = models.CharField(max_length=150)
    link3 = models.CharField(max_length=150)
    link4 = models.CharField(max_length=150)
    link5 = models.CharField(max_length=150)
    link6 = models.CharField(max_length=150)
    link7 = models.CharField(max_length=150)
    link8 = models.CharField(max_length=150)
    link9 = models.CharField(max_length=150)

class Images (models.Model):
    img1 = models.ImageField(default = 'static/images/banner.jpg')
    img2 = models.ImageField(default = 'static/images/banner.jpg')
    img3 = models.ImageField(default = 'static/images/banner.jpg')
    img4 = models.ImageField(default = 'static/images/banner.jpg')
    img5 = models.ImageField(default = 'static/images/banner.jpg')
    img6 = models.ImageField(default = 'static/images/banner.jpg')
    img7 = models.ImageField(default = 'static/images/banner.jpg')
    img8 = models.ImageField(default = 'static/images/banner.jpg')
    img9 = models.ImageField(default = 'static/images/banner.jpg')



class Users(models.Model):
    name = models.CharField(max_length=15)
    gmail = models.CharField(max_length=44)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    link = models.ForeignKey(Links,related_name='links',on_delete=models.CASCADE)
    images = models.ForeignKey(Images,related_name='Imag',on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name