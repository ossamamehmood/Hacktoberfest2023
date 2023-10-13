from django.db import models

# Create your models here

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=100)
    parent_number = models.CharField(max_length=100)

class Location(models.Model):
    last_location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)