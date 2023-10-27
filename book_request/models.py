from django.db import models

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="requests")
    title = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    year = models.IntegerField()
    subject = models.TextField()
    bookshelves = models.TextField()
    def __str__(self):
        return self.title