from typing import List
import uuid

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app import models
from app import exceptions

app = FastAPI()


@app.exception_handler(exceptions.DomainException)
def handle_invalid_usage(response, error):
    return JSONResponse(error.to_dict(), status_code=error.status_code)


"""Exercise 1 - instantiate PersonModel"""
items = [{"name": "John", "age": 45}, {"name": "Nancy", "age": 23}]


def _get_item(item_id):
    return next(filter(lambda item: item.id == item_id, items))


@app.get("/", response_model=models.ResponseModel)
def read_root():
    return models.ResponseModel(message="Hello World")


@app.get("/items/{item_id}", response_model=models.PersonModel)
def get_item(item_id: uuid.UUID):
    try:
        return _get_item(item_id)
    except StopIteration:
        raise exceptions.EntityNotFound("Item not found")


@app.get("/items", response_model=List[models.PersonModel])
def get_items():
    return items


@app.post("/items")
def add_item(person: dict):
    """Exercise 2 - Use PersonModel"""
    items.append(person)
    return person


@app.put("/items/{item_id}")
def update_item(item_id: uuid.UUID, address: dict):
    """Exercise 3 - Use AddressModel"""
    item = _get_item(item_id)
    item.address = address
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: uuid.UUID):
    """Exercise 5"""
    item = _get_item(item_id)
    items.remove(item)