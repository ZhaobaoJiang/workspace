from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.BooleanField(default=False)
    age = models.IntegerField(default=30)
    memo = models.TextField(default="hello")
    createdate = models.DateTimeField(default="2017-05-15 07:40") 
    typeId = models.ForeignKey('UserType')
    
class UserType(models.Model):
    name = models.CharField(max_length=50)
      
class Asset(models.Model):
    hostname = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    
class group(models.Model):
    name = models.CharField(max_length=50) 
    
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50) 
    group_relation = models.ManyToManyField('group')      