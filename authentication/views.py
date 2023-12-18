import json
import json
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers

from .models import Member
from user.models import Profile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

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

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print(username, password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.            
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
                "id": user.id,
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
@csrf_exempt
def logout_flutter(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": 'username_exists',
                "message": "Username already exists."
            }, status=400)
        
        # Create the new user
        user = User(username=username)
        user.set_password(password1)
        user.save()
        member = Member(account=user)
        member.save()
        member.account.password = password1
        profile = Profile(member=member, age=0, bio="")
        profile.save()
        
        return JsonResponse({
            "username": member.account.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

def show_json(request):
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")