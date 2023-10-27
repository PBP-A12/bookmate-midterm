from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponseNotFound, HttpResponseRedirect
from book_request.forms import ProductForm
from django.urls import reverse
from book_request.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def show_book(request):
    Books = Book.objects.all()
    context = {
        'name': '',
        'title': '',
        'lang': '',
        'first_name': '',
        'last_name': '',
        'year': '',
        'subject': '',
        'bookshelves': '',
    }
    return render(request, 'request.html', context)

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    product_item = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        title = request.POST.get("title")
        lang = request.POST.get("lang")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        year = request.POST.get("year")
        subject = request.POST.get("subject")
        bookshelves = request.POST.get("bookshelves")
        user = request.user

        books = Book.objects.all()
        existing_book = books.filter(name=name).first()
        if existing_book:
            return HttpResponse(b"EXIST", status=409) #edit this line
        else:
            new_product = Book(name=name, title=title, lang=lang, first_name=first_name, last_name=last_name, year=year, subject=subject, bookshelves=bookshelves, user=user)
            new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()