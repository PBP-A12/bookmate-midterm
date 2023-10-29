import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authentication.models import Member
from books.models import Book
from dashboardbuku.models import Review
from user.models import Profile
from django.core import serializers
# from book_request.models import BookRequest


@login_required(login_url='/auth/login/')
def user(request, id): 
    member = Member.objects.get(account=id)
    user = User.objects.get(pk=id)

    profile = Profile.objects.get(member=member)
    
    context = {
        "id" : id,
        "userProfile" : user,
        "profile" : profile,
        "subjects" : member.interest_subjects.all(),
    }
    return render(request, 'user.html', context)

def get_matched(request, id):
    member = Member.objects.get(account=id)

    matches = member.match_received.all()
    serialized_matches = serializers.serialize("json", matches)
    serialized_matches = json.loads(serialized_matches)

    for i in serialized_matches:
        user = User.objects.get(id=i["fields"]["account"])
        profile = Profile.objects.get(member__account__pk=i["fields"]["account"])

        serialized_user = serializers.serialize("json", [user])
        serialized_user = json.loads(serialized_user)
        i["user"] = serialized_user[0]

        serialized_profile = serializers.serialize("json", [profile])
        serialized_profile = json.loads(serialized_profile)
        i["profile"] = serialized_profile[0]
        
    
    return JsonResponse(serialized_matches, safe=False)

def get_reviews(request, id):
    member = Member.objects.get(account=id)
    review = Review.objects.filter(reviewer=member)

    serialized_matches = serializers.serialize("json", review)
    serialized_matches = json.loads(serialized_matches)

    for i in serialized_matches:
        book = Book.objects.get(id=i["fields"]["book"])

        serialized_user = serializers.serialize("json", [book])
        serialized_user = json.loads(serialized_user)
        i["book"] = serialized_user[0]
    
    return JsonResponse(serialized_matches, safe=False)
