from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from book_request.serializers import BookRequestSerializer
from match.models import Matching
from book_request.models import BookRequest
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from django.db.models import Max
import json 
import random


@login_required
def show_match(request): 
    delete_no_match()
    user_login = request.user
    context = {
        "user_login": user_login
    }
    return render(request, 'match.html', context=context) 

@login_required
@csrf_exempt
def get_match(request):
    this_member = Member.objects.get(account = request.user)
    other_member = None 
    for user_i in Member.objects.order_by("?") : 
        is_matched = Matching.objects.filter(user = this_member, matched_member = user_i, accepted = True).exists()
        if (user_i != this_member and not is_matched and not user_i.account.is_superuser) :
            other_member = user_i 
            break 
    
    if (other_member is None) : 
        return HttpResponseNotFound("No Member", status = 404)
  
    # other_profile = Profile.objects.get(member = other_member)
    new_match = Matching.objects.filter(user = this_member, matched_member = other_member, accepted = False)
    if (new_match) :
        new_match = new_match.first() 
    else : 
        new_match = Matching(user = this_member, matched_member = other_member)
    new_match.save()
    
    interest = "-"
    if (BookRequest.objects.filter(member = other_member).exists() and BookRequest.objects != None):
        user_book = BookRequest.objects.filter(member = other_member).first()
        user_books_serialized  = json.dumps(BookRequestSerializer(user_book, many=True).data)
        user_books_deserialized = json.load(user_books_serialized)
        for books in user_books_deserialized:
            interest = books('subjects')
    result = {
        "name" : other_member.account.username, 
        "first_name": other_member.account.first_name,
        "last_name": other_member.account.last_name,
        "id" : other_member.account.pk, 
        "matching_id" : new_match.pk,
        "interest_subject" : interest, # match_interest(this_member, other_member)
        "bio" :  "apa aja dulu" #other_profile.bio,
        # "profile_user" : "user/%other_member.account"
    }
    #print(result.interesting_subject)
    return HttpResponse(json.dumps(result), content_type="application/json")    # pass

@csrf_exempt
def accept_recommendation(request, id):
    recommendation = Matching.objects.get(pk=id)
    print(recommendation.matched_member)
    if request.user == recommendation.user.account:
        recommendation.accepted = True
        recommendation.save()
        if is_receiver(recommendation.user, recommendation.matched_member):
            recommendation.user.match_received.add(recommendation.matched_member)
            print("ini terima dari")
            print(recommendation.user.match_received.all())
        if not is_receiver(recommendation.user, recommendation.matched_member):
            recommendation.user.match_sent.add(recommendation.matched_member)
            print("ini nge send ke")
            print(recommendation.user.match_sent.all())
        return HttpResponseRedirect(reverse('match:show_match'))

def delete_no_match():
    notMatch_to_delete = Matching.objects.filter(accepted=False)
    notMatch_to_delete.delete()

def is_receiver(this_member, other_member):
    return Matching.objects.filter(user=other_member, matched_member=this_member, accepted=True).exists()

def get_sender_matches(received_user):
    sender_matches = []
    for sender_user in Member.objects.order_by("?"):
        if Matching.objects.filter(user=sender_user, matched_member=received_user, accepted=True).exists():
            sender_matches.append(sender_user)
    return sender_matches

def get_receiver_matches(sender_user):
    receiver_matches = []
    for received_user in Member.objects.order_by("?"):
        if Matching.objects.filter(user=sender_user, matched_member=received_user, accepted=True).exists():
            receiver_matches.append(received_user)
    return receiver_matches
    
def match_interest(this_member, other_member):
    BookRequest.objects.filter(member = other_member).first()
    set1 = set(this_member.interest_subjects.all())
    set2 = set(other_member.interest_subjects.all())
    intersection_result = set1.intersection(set2)
    if not intersection_result:
        interest_subject = random.choice(list(set2))
    else:
        interest_subject = random.choice(list(intersection_result))
    return interest_subject




        
    
