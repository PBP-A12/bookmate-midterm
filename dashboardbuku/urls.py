from django.urls import path
from dashboardbuku.views import *
# add_review_flutter, show_book, add_review_ajax, get_review_json, add_review_ajax2, get_titles, searchBookbyTitle,\
#                                 search_flutter

app_name = 'dashboardbuku'

urlpatterns = [
    path('', show_book, name='show_book'),
    path('get-review/<int:id>/', get_review_json, name='get_review_json'),
    path('create-review-ajax/<int:id>/', add_review_ajax, name='add_review_ajax'),
    path('add-review-ajax2/<int:id>/', add_review_ajax2, name='add_review_ajax2'),
    path('get-titles', get_titles, name='get_titles'),
    path('search/', searchBookbyTitle, name='search_book'),
    path('add-review-flutter/', add_review_flutter, name='add_review_flutter'),
    # path('get-all-review/', get_all_review_, name='get_all_review'),
    path('search-flutter/<str:judul>/', search_flutter, name='search_flutter'),
]