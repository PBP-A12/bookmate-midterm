from django.urls import path 
from .views import * 

app_name = 'home'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get_any_recommended_book', get_any_recommended_book, name='get_any_recommended_book'),
]