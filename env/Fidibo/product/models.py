from django.core.exceptions import ValidationError
from django.db import models 
from datetime import date, timedelta



class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=12)
    email = models.EmailField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="avatars/")    


class Authur(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    books = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/")


class Book(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField(max_length=200)
    price = models.PositiveIntegerField()
    avatar = models.ImageField(upload_to='avatars/')
    file = models.FileField(upload_to='documents/')





