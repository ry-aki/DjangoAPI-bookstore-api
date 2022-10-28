
# Bookstore API

A bookstore API, performing CRUD operations, written in Python django restframework.

## Functionalities

- GET request to fetch all books available.
- GET request to fetch books by id, title and author_name.
- POST request to add a new book. 
- PUT request to update information about a book by id.
- DELETE request to delete a book by id.


## API References

#### Get books all/ by id/ by title/ by author_name
```http
  GET /api/book-list/
  GET /api/book-list/id/{id}/
  GET /api/book-list/title/{title}/  
  GET /api/book-list/author-name/{author-name}/
```

#### Post/Add book  
```http
  POST /api/book-add/
```
#### Update book by id 
```http
  PUT /api/book-update/{id}/
```
#### Delete book by id 
```http
  DELETE /api/book-delete/{id}/
```

