from unicodedata import name
from django.db import models

# Create your models here.



class users(models.Model):
    name = models.CharField(max_length=15)
    gmail = models.CharField(max_length=44)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class links(models.Model):
    user = models.ForeignKey(users,on_delete=models.CASCADE)
    Link1 = models.CharField(max_length=150)
    Link2 = models.CharField(max_length=150)
    Link3 = models.CharField(max_length=150)
    Link4 = models.CharField(max_length=150)
    Link5 = models.CharField(max_length=150)
    Link6 = models.CharField(max_length=150)
    Link7 = models.CharField(max_length=150)
    Link8 = models.CharField(max_length=150)
    Link9 = models.CharField(max_length=150)
    Link10 = models.CharField(max_length=150)

 