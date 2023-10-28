from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from match.models import Matching
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from django.db.models import Max
import json 


@login_required
def show_match(request): 
    user_login = request.user
    context = {
        "user_login": user_login
    }
    return render(request, 'match.html', context=context) 

@login_required
@csrf_exempt
def get_match(request):
    this_user = Member.objects.get(account = request.user)
    other_user = None 

    for user_i in Member.objects.order_by("?") : 
        is_matched = Matching.objects.filter(user = this_user, matched_member = user_i, accepted = True).exists()
        if (user_i != this_user and not is_matched) :
            other_user = user_i 
            break 
    
    if (other_user is None) : 
        return HttpResponseNotFound("No Member", status = 404)
  
    new_match = Matching.objects.filter(user = this_user, matched_member = other_user, accepted = False)
    if (new_match) :
        new_match = new_match.first() 
    else : 
        new_match = Matching(user = this_user, matched_member = other_user)
    new_match.save()

    result = {
        "name" : other_user.account.username, 
        "id" : other_user.pk, 
        "matching_id" : new_match.pk
    }
    return HttpResponse(json.dumps(result), content_type="application/json")    # pass

@csrf_exempt
def accept_recommendation(request, id):
    recommendation = Matching.objects.get(pk=id)
    if request.user == recommendation.user.account:
        recommendation.accepted = True
        recommendation.save()
        return HttpResponseRedirect(reverse('match:show_match'))
    

    
