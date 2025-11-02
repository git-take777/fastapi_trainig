from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Book One", "author": "Author A", "category": "Fiction"},
    {"title": "Book Two", "author": "Author B", "category": "Non-Fiction"},
    {"title": "Book Three", "author": "Author C", "category": "Science Fiction"},
    {"title": "Book Four", "author": "Author D", "category": "Fantasy"},
    {"title": "Book Five", "author": "Author E", "category": "Biography"},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{title}")
async def read_book(title :str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
          return book