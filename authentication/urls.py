from django.urls import path 
from .views import * 

app_name = 'authentication' 

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login-flutter/', login_flutter, name='login_flutter'),
    path('register-flutter/', register_flutter, name='register_flutter'),
    path('logout-flutter/', logout_flutter, name='logout_flutter'),
    path('json/', show_json , name='json'),
]