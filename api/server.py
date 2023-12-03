from typing import Annotated
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import timedelta
import uvicorn
from books_db import books_db


from pydantic import BaseModel

class Book(BaseModel):
    name: str | None = None
    author: str | None = None
    year: int | None = None
    Description: str | None = None
    ISBN: str | None = None

class BookUseCases:
    def __init__(self, database: list[dict]):
        self.db = database

    def create_new_book(self, book: Book):
        books_db.append(book.dict())
        return book

    def get_all_books(self):
        return self.db
    
    def get_book_by_isbn(self, isbn: str):
        return list(filter(lambda item: (item["ISBN"] == isbn), self.db))

    def update_book(self, book_isbn: str, book: Book):
        _ , idx = self._find_book(book_isbn)

        if idx != -1:
            raise HTTPException(status_code=404, detail="Book not found")

        self.db[idx] = book.dict()
        return self.db[idx]

    def delete_book(self, book_isbn: str):
        book , idx = self._find_book(book_isbn)
        if idx != -1:
            del self.db[idx]
        return book

    def _find_book(self, isbn: str):
        for (idx, book) in enumerate(books_db):
            if book["ISBN"] == isbn:
                return (book, idx)
        return ({}, -1)


app = FastAPI()
book_use_cases = BookUseCases(database=books_db)

# Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/items/{ids}", response_class=HTMLResponse)
async def read_item_template(request: Request, ids: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": ids})







# Comienzo del router

@app.post("/api/v1/cookie")
def create_cookie(response: Response):
    response.set_cookie(key="mi_session", value="Hola", max_age=timedelta(days=7))
    return {"message": "Cookie agregada"}

@app.get("/api/v1/cookie")
def read_cookie(request: Request):
    cookie = request.cookies.get("mi_session")
    return {"cookie": f"La cookie dice {cookie}"}

@app.get("/api/v1/books/{book_id}")
async def get_book_by_isbn(book_isbn: str):
    return book_use_cases.get_book_by_isbn(book_isbn)

@app.get("/api/v1/books")
async def read_books():
    return book_use_cases.get_all_books()

@app.post("/api/v1/books")
async def create_book(book: Book):
    return book_use_cases.create_new_book(book)

@app.put("/api/v1/books/{book_id}")
async def update_book(book_id: str, book: Book):
    return book_use_cases.update_book(book_id, book)

def find_book(isbn: str):
    for (idx, book) in enumerate(books_db):
        if book["ISBN"] == isbn:
            return (book, idx)
    return ({}, -1)


@app.patch("/api/v1/books/{book_id}")
async def update_isbn(book_id: str, new_data: Book):
    _, idx = find_book(book_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Book not found")

    #TODO: Agregar logica para verificar que ciertos campos no vengan vacios.
    new_book = Book(**new_data.dict())

    books_db[idx] = new_book.dict()
    return new_book


@app.delete("/api/v1/books/{book_isbn}")
async def delete_book(book_isbn: str):
    book_use_cases.delete_book(book_isbn)


@app.get("/api/v2/custom_header")
def custom_header(response: Response):
    response.headers["Custom-Header"] = "Contenido del encabezado"
    return {"message": "header agregado con exito"}

@app.get("/api/v2/redirect")
def redirect_to_v1():
    response = RedirectResponse(url="http://localhost:8080/api/v1/books", status_code=307)
    return response
    

if __name__ == "__main__":
    config = uvicorn.Config("server:app", port=8080, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
