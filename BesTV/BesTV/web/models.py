from __future__ import unicode_literals

from django.db import models

# Create your models here.
class contact(models.Model):
    username = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    