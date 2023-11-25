from fastapi import FastAPI, HTTPException
import uvicorn
from books_db import books_db

from pydantic import BaseModel

class Book(BaseModel):
    name: str | None = None
    author: str | None = None
    year: int | None = None
    Description: str | None = None
    ISBN: str | None = None


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

def find_book(isbn: str):
    for (idx, book) in enumerate(books_db):
        if book["ISBN"] == isbn:
            return (book, idx)
    return ({}, -1)


@app.patch("/api/v1/books/{book_id}")
async def update_isbn(isbn: str, new_data: Book):
    book, idx = find_book(isbn)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Book not found")

    #TODO: Agregar logica para verificar que ciertos campos no vengan vacios.
    new_book = Book(**new_data.dict())

    books_db[idx] = new_book.dict()
    return new_book


@app.delete("/api/v1/books/{book_isbn}")
async def delete_book(book_isbn: str):
    _, idx = find_book(book_isbn)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[idx]
    return {"message": "Book deleted"}
    

if __name__ == "__main__":
    config = uvicorn.Config("server:app", port=8080, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
