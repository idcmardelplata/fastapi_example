from api.books_db import books_db
from api.server import app
from fastapi.testclient import TestClient
#TODO: Deberia poder elegirse por query parameter cual atributo de book modificar

    # obtener los libros
    # encontrar el libro buscado
    # modificar el isbn del libro buscado
    # actualizar base de datos en memoria 

def test_el_valor_isbn_del_libro_deberia_ser_actualizado():
    libro_encontrado = {}
    indice_encontrado:int = None
    isbn_a_cambiar = "978-0201616224"
    isbn_final = "ejemplo"
    for indice, libro in enumerate(books_db):
        if libro["ISBN"] == isbn_a_cambiar:
            libro_encontrado = libro
            indice_encontrado = indice
    libro_encontrado["ISBN"] = isbn_final
    books_db.pop(indice_encontrado)
    books_db.append(libro_encontrado)
    assert libro_encontrado["ISBN"] == isbn_final 
    assert books_db[len(books_db)-1]["ISBN"] == isbn_final

def test_el_servidor_deberia_actualizar_el_valor_de_isbn():
    sut = TestClient(app)
    id = "978-0984782857"
    old_isbn = sut.get("/api/v1/books/"+id).json()
    response = sut.patch("/api/v1/books/"+id,json={
        "name": "Cracking the Coding Interview",
        "author": "Gayle Laakmann McDowell",
        "year": "2015",
        "Description": "189 Programming Questions and Solutions",
        "ISBN": "prueba oeste puede"
      }).json()
    assert not response["ISBN"] == id
    

