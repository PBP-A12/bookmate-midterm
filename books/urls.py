from django.urls import path 
from .views import get_books, get_books_by_query, get_books_by_title, get_random_book

app_name = "books"

urlpatterns = [
    path("", get_books, name="get_books"), 
    path("search/", get_books_by_query, name="get_books_by_query"), 
    path("title/<str:title>/", get_books_by_title, name="get_books_by_title"), 
    path("random/", get_random_book, name="get_random_book")
]