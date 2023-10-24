from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model) : 
    # model subject / genre sebuah buku 
    name = models.CharField(max_length=255)     # nama subject tersebut, misalnya 'science fiction'

    def __str__(self): 
        return self.name

class Member(models.Model) : 
    # model 'user' BookMate, dinamai Member supaya tidak ambigu dengan model User bawaan Django 
    user = models.OneToOneField(User, on_delete=models.CASCADE)         # username dan email menggunakan model User bawaan Django
    subjects = models.ManyToManyField(Subject, related_name="members")  # subject-subject yang member sukai

    def __str__(self): 
        return self.user.username 