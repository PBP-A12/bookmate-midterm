from django.urls import include, path 
from match.views import *
from .views import show_match, get_match, accept_recommendation, redirect, get_match_flutter, accept_flutter

app_name = 'match'

urlpatterns = [
    path('', show_match, name='show_match'),
    path('get-match/', get_match, name='get_match'),
    path('accept/<int:id>/', accept_recommendation, name='accept'),
    path("user/<int:id>/", redirect, name="redirect"),
    path('get_match_flutter/', get_match_flutter, name='get_match_flutter'),
    path('accept-flutter/', accept_flutter, name='accept_flutter'),
]