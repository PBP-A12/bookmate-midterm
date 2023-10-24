from django.http import HttpResponse

import json 
from .models import Book 
from .serializers import BookSerializer

# Create your views here.
def get_books(request): 
    queryset = Book.objects.all()
    res = BookSerializer(queryset, many=True)
    return HttpResponse(json.dumps(res.data, indent=4), content_type='application/json')