from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model) : 
    name = models.CharField(max_length=255)

    def __str__(self): 
        return self.name

class Member(models.Model) : 
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name="members")

    def __str__(self): 
        return self.user.username 