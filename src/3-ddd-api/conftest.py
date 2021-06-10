import pytest

from fastapi.testclient import TestClient

from apps.api.entrypoint import app


@pytest.fixture
def client():
    return TestClient(app)
