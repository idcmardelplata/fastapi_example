
from pydantic import BaseModel
class Book(BaseModel):
    name: str
    author: str
    year: int
    Description: str
    ISBN: str

class UpdateBook:

    def __init__(self,db):
        self._db = db

    def update_isbn(self,book_id,book:Book):
        for libro in self._db:
            if libro["ISBN"] == book_id:
                libro["ISBN"] = book.ISBN
                return libro
