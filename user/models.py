from django.db import models
from authentication.models import Member

# Create your models here.

class Profile(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    age = models.IntegerField()
    bio = models.CharField(max_length=255)
