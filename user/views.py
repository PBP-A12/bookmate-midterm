from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from dashboardbuku.models import Review
from book_request.models import BookRequest


@login_required(login_url='/auth/login/')
def user(request, id): 
    member = Member.objects.get(pk=id)
    review = Review.objects.filter(reviewer=member)
    bookRequest = BookRequest.objects.filter(member=member)
    
    context = {
        "subjects" : member.interest_subjects.all(),
        "reviews" : review,
        "requests" : bookRequest
    }
    return render(request, 'user.html', context)