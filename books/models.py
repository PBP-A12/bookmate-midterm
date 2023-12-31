from django.db import models
from authentication.models import Subject 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    subjects = models.ManyToManyField(Subject)