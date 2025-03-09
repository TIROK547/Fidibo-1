from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.TextField(max_length=12)
    email = models.EmailField(null=True, blank=True)



class Book(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField(max_length=200)
    price = models.PositiveIntegerField()
    avatar = models.ImageField(upload_to='avatars/')
    file = models.FileField(upload_to='documents/')


