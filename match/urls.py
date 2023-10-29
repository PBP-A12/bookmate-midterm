from django.urls import include, path 
from match.views import *
from .views import show_match, get_match, accept_recommendation, redirect

app_name = 'match'

urlpatterns = [
    path('', show_match, name='show_match'),
    path('get-match/', get_match, name='get_match'),
    path('accept/<int:id>/', accept_recommendation, name='accept'),
    path("user/<int:id>/", redirect, name="redirect")
]