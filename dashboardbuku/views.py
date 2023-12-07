import json
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from books.models import Book
from dashboardbuku.models import Review
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from dashboardbuku.forms import ReviewForm
from authentication.models import Member
from books.serializers import BookSerializer

def show_book(request):
    books = Book.objects.all()
    forms = ReviewForm()
    books = BookSerializer(books, many=True)
    books = books.data
    context = {
        'books': books,
        'forms': forms
    }
    return render(request, "dashboardbuku.html", context)

def get_review_json(request, id):
    buku = Book.objects.get(pk = id)
    review_book = Review.objects.filter(book=buku).values("pk" ,"reviewer__account__username", "book", "review")
    return HttpResponse(json.dumps(list(review_book)), content_type='application/json')

# def get_all_review_(request):
#     buku = Book.objects.all()
#     review_book = Review.objects.filter(book=buku).values("pk" ,"reviewer__account__username", "book", "review")
#     return HttpResponse(json.dumps(list(review_book)), content_type='application/json')


@csrf_exempt
def add_review_ajax2(request, id):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        book = Book.objects.get(pk = id)
        review = data["value"]
        user = request.user
        member = Member.objects.get(account = user)
        new_review = Review(review=review, book=book, reviewer=member)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def add_review_ajax(request, id):
    book_review = Book.objects.get(pk = id)
    form = ReviewForm(request.POST or None, instance=book_review)
    book_review = BookSerializer(book_review)
    book_review = book_review.data
    user = request.user
    member = Member.objects.get(account = user)


    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.reviewer = request.reviewer
        review.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'book': book_review,
        'form': form,
        'member' : member
        }
    return render(request, "review.html", context)

def get_titles(request, titles):
    judul = Book.objects.filter(title__contains = titles)
    return HttpResponse(serializers.serialize('json'), judul)

def get_year (request, year):
    buku = Book.objects.filter(year__contains = year)

def searchBookbyTitle(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(title__icontains = query)
    data = [{
        'title': book.title,
        'author': book.author,
        'year': book.year,
    } for book in results]
    return JsonResponse(data, safe=False)



# Create your views here.
