from django.urls import re_path, path
from Bookstore import views


urlpatterns = [
    path('', views.api_overview, name = 'api_overview'),
    path('book-list/', views.BookAPI, name = 'book-list'),
    path(r'^books/([0-9]+)$', views.BookAPI)
]