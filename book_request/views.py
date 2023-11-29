from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from .forms import ProductForm
from django.urls import reverse
from book_request.models import BookRequest
from authentication.models import Member, Subject
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookRequestSerializer
import json
# Create your views here.

@login_required
def show_book(request):
    member = Member.objects.get(account=request.user)
    sort_by = request.GET.get('sortby')
    subjects = Subject.objects.all()
    subjects = subjects.values_list('name', flat=True)
    order = request.GET.get('sortorder', 'asc') # default to ascending order if not specified
    if sort_by:
        if order == 'asc':
            all_books = BookRequest.objects.all().order_by(sort_by)
            user_books = BookRequest.objects.filter(member=member).order_by(sort_by)
        elif order == 'desc':
            all_books = BookRequest.objects.all().order_by(f'-{sort_by}')
            user_books = BookRequest.objects.filter(member=member).order_by(f'-{sort_by}')
    else:
        all_books = BookRequest.objects.all()
        user_books = BookRequest.objects.filter(member=member)
    all_books_serialized  = json.dumps(BookRequestSerializer(all_books, many=True).data) 
    user_books_serialized  = json.dumps(BookRequestSerializer(user_books, many=True).data)
    # user_book_deserialized = json.loads(user_books_serialized)
    # for book in user_book_deserialized:
    #     print(book['subjects'])
    context = {
        'user': request.user,
        'title': '',
        'author': '',
        'year': '',
        'language': '',
        'subject': '',
        'date_requested': '',
        'all_books': all_books_serialized,
        'user_books': user_books_serialized,
        'subjects': subjects,
    }
    return render(request, 'request.html', context)

@csrf_exempt
def requesting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # print("AHHHHHH",title)
        author = request.POST.get('author')
        year = request.POST.get('year')
        language = request.POST.get('language')
        # print(request.POST)
        subject = request.POST.getlist('subject')
        user = Member.objects.get(account=request.user)
        if title != None or author != None or year != None or language != None or subject != None:
            # print('a')
            existing_book = BookRequest.objects.filter(title=title, author=author, year=year, language=language, subjects__name__in=subject).exists()
            if existing_book:
                # print('b')
                messages.info(request, 'This book has already been requested.')
            else:
                # print('c')
                book = BookRequest(member=user,title=title, author=author, year=year, language=language, date_requested=datetime.datetime.now())
                book.save()
                print(subject)
                for genre in subject:
                    print(Subject.objects.get(name=genre))
                    book.subjects.add(Subject.objects.get(name=genre))
                    print(book.subjects)
    else:
        messages.info(request, 'Please fill in all the fields.')
    return HttpResponse(b'CREATED', status=201)

@csrf_exempt
def edit_book(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        print("this",id)
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        language = request.POST.get('language')
        subjects = request.POST.get('subjects')
        book = BookRequest.objects.get(pk=id)
        book.title = title
        book.author = author
        book.year = year
        book.language = language
        book.subjects.set(subjects)
        book.save()
    return HttpResponse(b'CREATED', status=201)

@csrf_exempt
def delete_book(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book = BookRequest.objects.get(pk=id)
        book.delete()
    return HttpResponse(b'CREATED', status=201)

def get_request_json_user(request):
<<<<<<< Updated upstream
    res = BookRequestSerializer(BookRequest.objects.filter(member=Member.objects.get(account=request.user)), many=True).data
    
=======
    res = BookRequestSerializer(BookRequest.objects.filter(member=Member.objects.get(account=request.user)).order_by(request.GET.get('sortby')), many=True).data
>>>>>>> Stashed changes
    return HttpResponse(json.dumps(res, indent=4), content_type='application/json')

def get_requests_json(request):
    res = BookRequestSerializer(BookRequest.objects.all().order_by(request.GET.get('sortby')), many=True).data
    return HttpResponse(json.dumps(res, indent=4), content_type='application/json')

def get_subjects_json(request):
    data = serializers.serialize('json', Subject.objects.all())
    return HttpResponse(data, content_type='application/json')

# def get_requests_json_user_sort(request):
#     res = BookRequestSerializer(BookRequest.objects.filter(member=Member.objects.get(account=request.user)).order_by(request.GET.get('sortby')), many=True).data
#     return HttpResponse(json.dumps(res, indent=4), content_type='application/json')

# def get_requests_json_sort(request):
#     res = BookRequestSerializer(BookRequest.objects.all().order_by(request.GET.get('sortby')), many=True).data
#     return HttpResponse(json.dumps(res, indent=4), content_type='application/json')

@csrf_exempt
def edit_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data['id']
        title = data['title']
        author = data['author']
        year = data['year']
        language = data['language']
        subjects = data['subjects']
        book = BookRequest.objects.get(pk=id)
        book.title = title
        book.author = author
        book.year = year
        book.language = language
        book.subjects.set(subjects)
        book.save()
        return JsonResponse({
            "status": 'success',
            "message": "Request edited successfully!"
        }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

@csrf_exempt
def delete_request(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book = BookRequest.objects.get(pk=id)
        book.delete()
        return JsonResponse({
            "status": 'success',
            "message": "Request deleted successfully!"
        }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)