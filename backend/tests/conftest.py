### tests/conftest.py

import pytest

from app.main import app
from fastapi.testclient import TestClient
from app.repositories.items import items_repository


@pytest.fixture
def client(reset_repository):
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_repository():
    items_repository._items.clear()
    items_repository._next_id = 1