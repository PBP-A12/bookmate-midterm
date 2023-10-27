from django.shortcuts import render
from books.models import Book

def show_book(request):
    books = Book.objects.all()
    print(books[0].subjects)
    context = {
        'books': books
    }
    return render(request, "dashboardbuku.html", context)
# Create your views here.
