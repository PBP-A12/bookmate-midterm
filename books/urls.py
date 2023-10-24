from django.urls import path 
from .views import get_books, get_books_by_query

app_name = "books"

urlpatterns = [
    path("", get_books, name="get_books"), 
    path("search/", get_books_by_query, name="get_books_by_query"), 
]