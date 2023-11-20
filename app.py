from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

books = []

class Books(BaseModel):
    id: Optional[str]
    name:str
    author:str
    edit:str
    published: datetime = datetime.now()

app = FastAPI()

@app.get("/")
def index():
    return {'message':"Welcome to my API"}

@app.get("/books")
def show_books():
    return books

@app.post("/books")
def add_book(book: Books):
    books.append(book.model_dump())
    return books[-1] #ultimo libro agregado

@app.get("/book/{id}")
def show_book(id:str):
    for book in books:
        if book["id"] == id:
            return book
    return "400 error"

@app.put("/book/{id}")
def update_book(id:str, upbook:Books):
    for indice, book in enumerate(books):
        if book["id"] == id:
            book["name"] = upbook.name
            book["author"] = upbook.author
            book["edit"] = upbook.edit
            return "sucesses delete"
    return "400 error"

@app.delete("/book/{id}")
def delete_book(id:str):
    for indice, book in enumerate(books):
        if book["id"] == id:
            books.pop(indice)
            return "sucesses delete"
    return "400 error"