from django.urls import path 
from .views import * 

app_name = 'user'

urlpatterns = [
    path('<int:id>', user, name='user'),
    path('get_matched/<int:id>', get_matched, name='user'),
    path('get_reviews/<int:id>', get_reviews, name='user'),
]