from django.urls import path 
from .views import * 

app_name = 'user'

urlpatterns = [
    path('<int:id>', user, name='user'),
    path('get_matched/<int:id>', get_matched, name='get_matched'),
    path('get_reviews/<int:id>', get_reviews, name='get_reviews'),
    path('edit_profile/<int:id>', edit_profile, name='edit_profile'),
]