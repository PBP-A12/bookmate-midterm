from django.db import models
import datetime
from authentication.models import Member
from authentication.models import Subject

# Create your models here.
class BookRequest(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="requests")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    language = models.CharField(max_length=2)
    subjects = models.ManyToManyField(Subject)
    date_requested = models.DateTimeField(auto_now=True)

