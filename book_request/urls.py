from django.urls import include, path
from book_request.views import show_book, show_xml, show_json, show_xml_by_id, show_json_by_id, get_product_json, add_book_ajax
app_name = 'book_request'

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('/request', show_book, name='show_request'),
    path('/xml', show_xml, name='show_xml'),
    path('/json', show_json, name='show_json'),
    path('/xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('/json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('/get_product_json', get_product_json, name='get_product_json'),
    path('/add_book_ajax', add_book_ajax, name='add_book_ajax'),
]