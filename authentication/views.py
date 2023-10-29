from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers

from .models import Member
from user.models import Profile

# Create your views here.
def register(request): 
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            account = form.save()
            
            member = Member(account=account)
            member.save()

            # create profile 
            profile = Profile(member=member, age=0, bio="")
            profile.save()

            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
        
        else:
            context = {'form': form}
            return render(request, 'register.html', context)
        
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # serialized_obj = serializers.serialize('json', [ user ])
            # print(serialized_obj)
            login(request, user)
            response = HttpResponseRedirect(reverse("home:show_main")) 
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request): 
    logout(request)
    return redirect('home:show_main')