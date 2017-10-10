from django.db import models
from datetime import date

DATE_INPUT_FORMATS = ('%d-%m-%Y')


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=30)
    birthdate = models.DateField(default=date.today)
    gender = models.CharField(max_length=6)
    description = models.CharField(max_length=100)
    email = models.EmailField()

class Expertise(models.Model):
    expertise = models.CharField(max_length=255)

class PhotoURL(models.Model):
    model_pic = models.CharField(max_length=255)

