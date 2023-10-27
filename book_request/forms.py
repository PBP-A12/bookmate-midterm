from django.forms import ModelForm
from .models import BookRequest

class ProductForm(ModelForm):
    class Meta:
        model = BookRequest
        fields = ['title', 'author', 'year', 'language', 'subjects']