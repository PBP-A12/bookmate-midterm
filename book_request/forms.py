from django.forms import ModelForm
from book_request.models import Book

class ProductForm(ModelForm):
    class Meta:
        model = Book
        fields = ["user", "title", "lang", "first_name","last_name", "year","subject","bookshelves"]