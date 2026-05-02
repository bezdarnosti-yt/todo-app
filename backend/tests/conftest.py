### tests/conftest.py

import pytest

from app.main import app
from fastapi.testclient import TestClient
from app.repositories.items import ItemsRepository
from app.dependencies import get_items_repository


@pytest.fixture
def client():
    items_repository = ItemsRepository()
    app.dependency_overrides[get_items_repository] = lambda: items_repository
    yield TestClient(app)
    app.dependency_overrides.clear()
