from servicios.updatebook import UpdateBook
from fastapi import FastAPI
import uvicorn
from api.books_db import books_db

from pydantic import BaseModel

class Book(BaseModel):
    name: str
    author: str
    year: int
    Description: str
    ISBN: str

app = FastAPI()


# Comienzo del router

@app.get("/api/v1/books/{book_id}")
async def read_books(book_id):
    """Return book id"""
    return list(filter(lambda item: (item["ISBN"] == book_id), books_db))

@app.get("/api/v1/books")
async def read_books():
    """Return all books"""
    return books_db

@app.post("/api/v1/books")
async def create_book(book: Book):
    books_db.append(book.dict())
    return book

@app.put("/api/v1/books/{book_id}")
async def update_book(book_id: str, book: Book):
    update_db = [ book if item["ISBN"] == book_id else item for item in books_db]
    books_db = update_db
    return book



@app.patch("/api/v1/books/{book_id}")
async def update_isbn(book_id: str, book: Book):
    return UpdateBook(books_db).update_isbn(book_id, book)

@app.delete("/api/v1/books/{book_id}")
async def delete_book(book_id):
    pass



if __name__ == "__main__":
    config = uvicorn.Config("server:app", port=8080, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
