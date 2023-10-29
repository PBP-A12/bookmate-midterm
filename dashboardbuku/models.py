from django.db import models
from books.models import Book
from authentication.models import Member
 
class Review(models.Model):
    reviewer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
# Create your models here.
