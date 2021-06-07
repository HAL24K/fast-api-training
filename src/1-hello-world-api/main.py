from typing import Optional

from fastapi import FastAPI

app = FastAPI()


items = [{'name': 'John', 'age': 45}, {'name': 'Nancy', 'age': 23}]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Exercise 1"""
    try:
        return items[item_id]
    except IndexError:
        return {"message": "Item not found"}


@app.get("/items")
def get_items():
    """Exercise 2"""
    pass


@app.post("/items")
def add_item():
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