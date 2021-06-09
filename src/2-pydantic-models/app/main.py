from typing import List

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app import models
from app import exceptions

app = FastAPI()


@app.exception_handler(exceptions.DomainException)
def handle_invalid_usage(response, error):
    return JSONResponse(error.to_dict(), status_code=error.status_code)


items = [{'name': 'John', 'age': 45}, {'name': 'Nancy', 'age': 23}]


@app.get("/", response_model=models.ResponseModel)
def read_root():
    return models.ResponseModel(message="Hello World")


@app.get("/items/{item_id}", response_model=models.PersonModel)
def get_item(item_id: int):
    """Exercise 1"""
    try:
        return items[item_id]
    except IndexError:
        raise exceptions.EntityNotFound("Item not found")


@app.get("/items", response_model=List[models.PersonModel])
def get_items():
    """Exercise 2"""
    pass


@app.post("/items")
def add_item(person: dict):
    """Exercise 3"""
    pass


@app.put("/items/{item_id}")
def update_item():
    """Exercise 4"""
    pass


@app.delete("/items/{item_id}")
def delete_item():
    """Exercise 5"""
    pass