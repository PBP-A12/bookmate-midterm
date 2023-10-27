from django.urls import path
from dashboardbuku.views import show_book

app_name = 'dashboardbuku'

urlpatterns = [
    path('', show_book, name='show_book'),
]