from django.urls import include, path
from book_request.views import show_book, get_request_json_user, requesting, get_requests_json, edit_book, delete_book, get_subjects_json
app_name = 'book_request'

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('', show_book, name='show_request'),
    path('requesting/', requesting, name='requesting'),
    path('get-request_json_user/', get_request_json_user, name='get_request_json_user'),
    path('get-requests_json/', get_requests_json, name='get_requests_json'),
    path('edit-book/', edit_book, name='edit_book'),
    path('delete-book/', delete_book, name='delete_book'),
    path('get-subjects-json/', get_subjects_json, name='get_subjects_json'),
]