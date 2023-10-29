from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def which_home(request): 
    return 3

# Create your views here.
def show_main(request): 
    if (request.user.is_authenticated): 
        context = {
            'home': which_home(request),
        }
        return render(request, 'home.html', context=context) 
    return render(request, 'landing.html')