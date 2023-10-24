from django.http import HttpResponse

import json 
from .models import Book 
from .serializers import BookSerializer

# Create your views here.
def get_books(request): 
    queryset = Book.objects.all()
    res = BookSerializer(queryset, many=True)
    return HttpResponse(json.dumps(res.data, indent=4), content_type='application/json')

def get_books_by_query(request):
    query = request.GET.get('search', '').strip()  
    rquery = query.lower() + '+'
    queryset = Book.objects.filter(title__iregex=rquery); 
    print(queryset)
    res = BookSerializer(queryset, many=True)
    return HttpResponse(json.dumps(res.data, indent=4), content_type='application/json')