from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_main(request): 
    
    return render(request, 'main.html')

@login_required(login_url='/login')
def authenticated_home(request): 
    pass