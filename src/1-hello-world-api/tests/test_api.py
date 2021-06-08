from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_items():
    pass


def test_add_item():
    pass


def test_update_item():
    pass


def test_delete_item():
    pass