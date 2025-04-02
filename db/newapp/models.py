from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length= 100,primary_key=True)
    age = models.IntegerField()
    email = models.EmailField()
    # image = models.ImageField()
    # def __str__(self):
    #     return f'{self.name}--{self.age}'
