from django.urls import path 
from .views import * 

app_name = 'home'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('test/', test, name='test'),
]