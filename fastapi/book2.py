from fastapi import FastAPI
app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    def __init__(self,id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, "Book One", "Author A", "Description A", 4.5),
    Book(2, "Book Two", "Author B", "Description B", 4.0),
    Book(3, "Book Three", "Author C", "Description C", 5.0),
]
@app.get("/books/")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)

@app.post("/create-book")
async def create_book(book_request: Book):
    # **book_dataは自動的に↓こうなります:
# pythonBook(title="ハリー・ポッター", author="J.K.ローリング", pages=464)
# つまり、辞書の中身を一つ一つ書かなくても、まとめて渡せる便利な書き方なんです!
    new_book = BOOKS.append(**book_request.dict())
    BOOKS.append(new_book)
    return BOOKS

