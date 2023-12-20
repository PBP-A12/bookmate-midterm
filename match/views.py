import logging
import time
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponseServerError, JsonResponse
from django.urls import reverse
from django.core import serializers
import requests
from book_request.serializers import BookRequestSerializer
from django.core.serializers import serialize
from match.models import Matching
from user.models import Profile
from book_request.models import BookRequest
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from django.db.models import Max
import json 
import random


user_avatars = {}


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
  
    other_profile = Profile.objects.get(member = other_member)
    new_match = Matching.objects.filter(user = this_member, matched_member = other_member, accepted = False)
    if (new_match) :
        new_match = new_match.first() 
    else : 
        new_match = Matching(user = this_member, matched_member = other_member)
    new_match.save()
    
    interest = get_interest(other_member)
    result = {
        "name" : other_member.account.username, 
        "first_name": other_member.account.first_name,
        "last_name": other_member.account.last_name,
        "id" : other_member.account.pk, 
        "matching_id" : new_match.pk,
        "interest_subject" : interest, # match_interest(this_member, other_member)
        "bio" :  other_profile.bio,
    }
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
            recommendation.matched_member.match_received.add(recommendation.user.match_received)
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
    

def get_interest(other_member):
    other_interest_book = BookRequest.objects.filter(member=other_member).first()

    if not other_interest_book:
        return ""
    # Extract names directly from the ManyToManyField
    interest_names = other_interest_book.subjects.values_list('name', flat=True)
    # Take only the first 3 subjects
    interest_names = list(interest_names)[:3]
    # Join the names into a single string separated by commas
    interest_string = ', '.join(interest_names)

    return interest_string

def get_matching_flutter(request):
    this_member = Member.objects.get(account = request.user)

def get_match_json(request):
    data = serializers.serialize('json', Matching.objects.all())
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def accept_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        matching_id = data['matching_id']
        recommendation = Matching.objects.get(pk=matching_id)
                                            #   matched_member=Member.objects(account=name))

        if Member.objects.get(account = request.user) == recommendation.user:
            recommendation.accepted = True
            recommendation.save()

            if is_receiver(recommendation.user, recommendation.matched_member):
                recommendation.user.match_received.add(recommendation.matched_member)
                print(recommendation.matched_member.match_received.all())
                recommendation.matched_member.match_received.add(recommendation.user)

            if not is_receiver(recommendation.user, recommendation.matched_member):
                recommendation.user.match_sent.add(recommendation.matched_member)

            return JsonResponse({
                "status" : "success",
                'message': ''
            }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": ""
        }, status=401)

# @login_required
@csrf_exempt   # disini
def get_match_flutter(request):
    this_member = Member.objects.get(account=request.user)
    other_member = None

    for user_i in Member.objects.order_by("?"):
        is_matched = Matching.objects.filter(user=this_member, matched_member=user_i, accepted=True).exists()
        if (user_i != this_member and not is_matched and not user_i.account.is_superuser):
            other_member = user_i
            break

    if other_member is None:
        return HttpResponseNotFound("No Member", status=404)

    other_profile = Profile.objects.get(member=other_member)
    if (other_profile.bio is None):
        other_profile.bio = ""
        other_profile.save()
    new_match = Matching.objects.filter(user=this_member, matched_member=other_member, accepted=False)

    if new_match:
        new_match = new_match.first()
    else:
        new_match = Matching(user=this_member, matched_member=other_member)
        new_match.save()

    interest = get_interest_flutter(other_member)
    result = {
        "name": other_member.account.username,
        "first_name": other_member.account.first_name,
        "last_name": other_member.account.last_name,
        "id": other_member.account.pk,
        "matching_id": new_match.pk,
        "interest_subject": interest,
        "bio": other_profile.bio,
        "picture" : get_picture_for_user(other_member.account.username)  ,
    }
    logging.info('get_match endpoint reached successfully')

    return JsonResponse(result)


def get_interest_flutter(other_member):
    try:
        other_interest_book = BookRequest.objects.filter(member=other_member)
        print(other_interest_book)
        
        if not other_interest_book:
            return []
        
        # Extract names directly from the ManyToManyField
        interest_names = [book.subjects.values_list('name', flat=True) for book in other_interest_book]
        # Flatten the list of lists
        interest_names = [item for sublist in interest_names for item in sublist]
        # Take only the first 3 subjects
        interest_names = interest_names[:3]
        # Join the names into a single string separated by commas
        return interest_names
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def get_picture_for_user(username):
    if username not in user_avatars:
        # Jika avatar belum ada untuk user tertentu, buat dan simpan
        user_avatars[username] = get_random_image_url(username)
    return user_avatars[username]

def get_random_image_url(username):
    unique_identifier = hash(username)  # Gunakan ID pengguna atau sesuatu yang unik sebagai basis
    return 'https://picsum.photos/200/300?random=' + str(unique_identifier)



from user.views import user

@login_required
def redirect(request, id) : 
    return user(request, id)