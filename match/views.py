from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from match.models import Matching
from match.forms import MatchingForm
from django.contrib.auth.decorators import login_required
from authentication.models import Member
import random
from django.db.models import Max

import json 
# Create your views here.

@login_required
def show_match(request): 
    user_login = request.user

    context = {
        "user_login": user_login
    }
    return render(request, 'match.html', context=context) 

# ajax lewat js di html, terserah async await, atau pakai jquery
# disini jadi ajax
@login_required
@csrf_exempt
def get_match(request):
    this_user = Member.objects.get(account = request.user)
    other_user = get_random()
    is_matched = Matching.objects.filter(user = this_user, matched_member = other_user, accepted = True).exists()
    while (this_user.id == other_user.id or is_matched):
        other_user = get_random()
        is_matched = Matching.objects.filter(user = this_user, matched_member = other_user, accepted = True).exists()
    
    new_match = Matching(user = this_user, matched_member = other_user)
    new_match.save()
    print("sampe sini oke")
    print(other_user)
    result = {
        "name" : other_user.account.username, 
        "id" : other_user.pk
    }
    return HttpResponse(json.dumps(result), content_type="application/json")    # pass
    
    ## kita get random saja dulu
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user
    # fokusnya ketika get_match dipanggil harusnya kembalikan random user

def accept_recommendation(request, id):
    recommendation = Matching.objects.filter(pk=id)
    print("masuk guys")
    if request.matched_member == recommendation.matched_member:
        recommendation.accepted = True
        recommendation.save()
        print("hiiiiiiii")
        return HttpResponseRedirect(reverse('show_match'))
    
def get_random():
   max_id = Member.objects.all().aggregate(max_id=Max("id"))['max_id']
   while True:
    pk = random.randint(0, max_id)
    member_matched = Member.objects.filter(pk=pk).first()
    if member_matched:
        return member_matched
    
