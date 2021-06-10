import uuid

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_item():
    uuid = "5152cda2-db25-4338-8ffa-77923f2c885f"
    response = client.get(f"/items/{uuid}")

    assert response.status_code == 200
    assert response.json()["name"] == "John"


def test_add_item():
    data = {"name": "Sam", "age": 25}
    response = client.post("/items", json=data)

    assert response.status_code == 200
    assert type(uuid.UUID(response.json()["id"])) is uuid.UUID


def test_update_item():
    uuid = "5152cda2-db25-4338-8ffa-77923f2c885f"
    data = {"street": "Main Street"}
    response = client.put(f"/items/{uuid}", json=data)

    assert response.status_code == 200
    assert response.json()["address"]["street"] == "Main Street"


def test_delete_item():
    uuid = "5152cda2-db25-4338-8ffa-77923f2c885f"
    client.delete(f"/items/{uuid}")

    response = client.get(f"/items/{uuid}")

    assert response.status_code == 404