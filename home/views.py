from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from dashboardbuku.models import Review
from authentication.models import Member
import json 
from django.http import HttpResponse

def which_home(request): 

    # kalau profil belum lengkap, 1 
    # kalau belum ada review, 2 
    member = Member.objects.get(account=request.user)
    have_reviewed = Review.objects.filter(reviewer=member).count() > 0
    if (not have_reviewed): 
        return 2
    # sisanya 3 
    return 3

# Create your views here.
def show_main(request): 
    if (request.user.is_authenticated): 
        context = {
            'home': which_home(request),
        }
        return render(request, 'home.html', context=context) 
    return render(request, 'landing.html')
