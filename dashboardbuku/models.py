from django.db import models
from books.models import Book
from authentication.models import Member
 
class Review(models.Model):
    reviewer = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
# Create your models here.
