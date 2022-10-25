from enum import unique
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Bookstore.models import BookModel
from Bookstore.serializers import BookSerializer
"""
def api_overview(request):
    api_urls = {
        'List' : '/book-list/',
        'Detail View' : '/book-detail/<int:id>/',
        'Add' : '/book-add/',
        'Update' : '/book-update/<int:id>/',
        'Delete' : '/book-delete/<int:id>/',
    }
    return JsonResponse(api_urls)
"""
@csrf_exempt
def BookAPI(request, id = 0):
    # GET- get all records
    if request.method == 'GET':
        books = BookModel.objects.all()
        books_serializer = BookSerializer(books, many = True)
        return JsonResponse(books_serializer.data, safe = False)

    # POST - post/add a new book's data
    elif request.method == 'POST':
        books_input_data = JSONParser().parse(request)
        books_serializer = BookSerializer(data = books_input_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Added Successfully :)", safe = False)
        return JsonResponse("Failed to add :(", safe = False) 

    # PUT - update a book's data based on id input      
    elif request.method == 'PUT':
        books_input_data = JSONParser().parse(request)
        book_record_selected = BookModel.objects.get(unique_id = books_input_data['unique_id'])
        books_serializer = BookSerializer(book_record_selected, data = books_input_data) 
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Updated Successfully :)", safe = False)
        else:
            return JsonResponse("Update Failed :(", safe = False)

    # DELETE - delete a record based on id input. 
    elif request.method == 'DELETE':
        book_record_selected = BookModel.objects.get(unique_id = id)
        book_record_selected.delete()
        return JsonResponse("Deleted Successfully :)", safe = False)

