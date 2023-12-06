from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.models import Book
from dashboardbuku.models import Review
from authentication.models import Member
from django.http import HttpResponse
from books.views import get_random_book

def which_home(request): 
    # kalau profil belum lengkap, 1 
    # kalau belum ada review, 2 
    member = Member.objects.get(account=request.user)
    if (member.profile.age == 0 or member.profile.bio == ""): 
        return 1
    have_reviewed = Review.objects.filter(reviewer=member).count() > 0
    if (not have_reviewed): 
        return 2
    # sisanya 3 
    return 3

# Create your views here.
def show_main(request): 
    if (request.user.is_authenticated):
        if (Member.objects.filter(account=request.user).count() == 0):
            # this user ga punya member object hiks 
            # bikin member baru 
            member = Member(account=request.user)
            member.save()
            
        context = {
            'home': which_home(request),
        }
        return render(request, 'home.html', context=context) 
    return render(request, 'landing.html')

@login_required
def get_any_recommended_book(request): 
    # anggap aja rekomendasi hehe
    return get_random_book(request)