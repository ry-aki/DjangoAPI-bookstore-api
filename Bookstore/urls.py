from django.urls import path
from . import views


urlpatterns = [
    # path('', views.api_overview, name = 'api_overview'),
    
    path('book-list/', views.GetAll, name = 'book-list'),
    path('book-list/id/<int:input_id>/', views.ViewBookById, name = 'book-detail-by-id'),    
    path('book-list/title/<str:input_title>/', views.ViewBookByTitle, name = 'book-detail-by-title'),    
    path('book-list/author/<str:input_author_name>/', views.ViewBookByAuthorName, name = 'book-detail-by-author-name'),

    path('book-add/', views.AddBook, name = 'book-add'),
    path('book-update/<int:input_id>/', views.UpdateBook, name = 'book-update'),
    path('book-delete/<int:input_id>/', views.DeleteBook, name = 'book-delete'),
    
]