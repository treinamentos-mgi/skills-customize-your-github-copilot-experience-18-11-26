from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Book API",
    description="A REST API for managing a collection of books.",
)


class Book(BaseModel):
    title: str
    author: str
    year: int


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# Task 2: Add GET /books and POST /books.
# Task 3: Add GET, PUT, and DELETE routes for /books/{book_id}.
