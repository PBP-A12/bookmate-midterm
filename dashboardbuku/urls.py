from django.urls import path
from dashboardbuku.views import show_book, add_review_ajax, get_review_json, add_review_ajax2, get_titles, searchBookbyTitle

app_name = 'dashboardbuku'

urlpatterns = [
    path('', show_book, name='show_book'),
    path('get-review/<int:id>/', get_review_json, name='get_review_json'),
    path('create-review-ajax/<int:id>/', add_review_ajax, name='add_review_ajax'),
    path('add-review-ajax2/<int:id>/', add_review_ajax2, name='add_review_ajax2'),
    path('get-titles', get_titles, name='get_titles'),
    path('search/', searchBookbyTitle, name='search_book')
]