from enum import unique
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Bookstore.models import BookModel
from Bookstore.serializers import BookSerializer
from Bookstore import serializers

"""@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List' : '/book-list/',
        'Detail View' : '/book-detail/<int:unique_id>/',
        'Detail View' : '/book-detail/title/<str:title>/',
        'Detail View' : '/book-detail/author/<str:author_name>/'
        'Add' : '/book-add/',
        'Update' : '/book-update/<int:id>/',
        'Delete' : '/book-delete/<int:id>/',
    }
    return Response(api_urls)"""

@api_view(['GET'])
def GetAll(request):
    # GET- get all records
    books = BookModel.objects.all()
    books_serializer = BookSerializer(books, many = True)
    return Response(books_serializer.data)

@api_view(['GET'])
def ViewBookById(request, input_id = 0):
    # GET - get record of particular book based on id input
    book = BookModel.objects.get(unique_id = input_id)
    book_serializer = BookSerializer(book, many = False)
    return Response(book_serializer.data)

@api_view(['GET'])
def ViewBookByTitle(request, input_title):
    # GET - get record of particular book based on book title
    book = BookModel.objects.filter(title = input_title)
    book_serializer = BookSerializer(book, many = True)
    return Response(book_serializer.data)   

@api_view(['GET'])
def ViewBookByAuthorName(request, input_author_name):
    # GET - get record of particular book based on author's name
    book = BookModel.objects.filter(author_name = input_author_name)
    book_serializer = BookSerializer(book, many = True)
    return Response(book_serializer.data)     
    
@api_view(['POST'])
def AddBook(request):
    # POST - post/add a new book's data
    book_serializer = BookSerializer(data = request.data)
    if book_serializer.is_valid():
        book_serializer.save()
        return Response("Added Successfully :)\n", book_serializer.data)
    return Response("Failed to add :(") 

@api_view(['PUT'])
def UpdateBook(request, input_id = 0):
    # PUT - update a book's data based on id input  
    book = BookModel.objects.get(unique_id = input_id)
    book_serializer = BookSerializer(instance = book, data = request.data) 
    if book_serializer.is_valid():
        book_serializer.save()
        return Response("Updated Successfully :)", book_serializer.data)
    else:
        return Response("Update Failed :(")

@api_view(['DELETE'])
def DeleteBook(request, input_id = 0):
    # DELETE - delete a record based on id input. 
    book = BookModel.objects.get(unique_id = input_id)
    book.delete()
    return Response("Deleted Successfully :)")