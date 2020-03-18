from django.db import models
from django.conf import settings


class Item(models.Model):
    sold = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    numberBought = models.IntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    gender = models.CharField(max_length=100)
    username = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=500, default='')

        
class Authenticator(models.Model):
    user_id = models.IntegerField(default=0)
    authenticator = models.CharField(max_length=255, primary_key=True)
    is_Valid = models.BooleanField(default=True)
    date_created = models.CharField(max_length=50)