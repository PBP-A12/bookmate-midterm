from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect
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

# Create your views here.

@login_required
def show_book(request):
    member = Member.objects.get(account=request.user)
    sort_by = request.GET.get('sortby')
    subjects = Subject.objects.all()
    subjects = subjects.values_list('name', flat=True)
    order = request.GET.get('order', 'asc') # default to ascending order if not specified
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
    context = {
        'user': request.user.username,
        'title': '',
        'author': '',
        'year': '',
        'language': '',
        'subject': '',
        'date_requested': '',
        'all_books': all_books,
        'user_requested': user_books,
        'subjects': subjects,
    }
    return render(request, 'request.html', context)

@csrf_exempt
def requesting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print("AHHHHHH",title)
        author = request.POST.get('author')
        year = request.POST.get('year')
        language = request.POST.get('language')
        subject = request.POST.getlist('subjects')
        user = Member.objects.get(account=request.user)
        if title != None or author != None or year != None or language != None or subject != None:
            existing_book = BookRequest.objects.filter(title=title, author=author, year=year, language=language, subjects__name__in=subject).exists()
            if existing_book:
                messages.info(request, 'This book has already been requested.')
            else:
                book = BookRequest(member=user,title=title, author=author, year=year, language=language )
                book.subjects.set(subject.toString())
                book.save()
    else:
        messages.info(request, 'Please fill in all the fields.')
    return HttpResponseRedirect('book_request:show_request')

@csrf_exempt
def edit_book(request):
    if request.method == 'POST':
        id = request.POST.get("id")
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
    if request.method == 'DELETE':
        id = request.DELETE.get('id')
        book = BookRequest.objects.get(pk=id)
        book.delete()
    return HttpResponse(b'CREATED', status=201)

def get_request_json_user(request):
    data = serializers.serialize('json', BookRequest.objects.filter(member=request.user))
    return HttpResponse(data, content_type='application/json')

def get_requests_json(request):
    data = serializers.serialize('json', BookRequest.objects.all())
    return HttpResponse(data, content_type='application/json')

def get_subjects_json(request):
    data = serializers.serialize('json', Subject.objects.all())
    return HttpResponse(data, content_type='application/json')