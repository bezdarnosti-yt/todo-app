### tests/test_items.py

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_item(client):
    response = client.post(
        "/items",
        json={"name": "test"}
    )
    assert response.status_code == 201
    assert response.json() == {"item_id": 1, "name": "test"}

    list_response = client.get("/items")
    assert list_response.json() == [{"item_id": 1, "name": "test"}]

def test_list_items_empty(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_list_items_after_create(client):
    client.post(
        "/items",
        json={"name": "123"}
    )
    client.post(
        "/items",
        json={"name": "456"}
    )
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == [
        {"item_id": 1, "name": "123"},
        {"item_id": 2, "name": "456"}
    ]

def test_get_item_by_id(client):
    client.post(
        "/items",
        json={"name": "123"}
    )
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "123"}

def test_get_item_not_found(client):
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

def test_update_item(client):
    client.post(
        "/items",
        json={"name": "123"}
    )
    response = client.patch(
        "/items/1",
        json={"name": "new"}
    )
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "new"}

def test_update_item_partial(client):
    client.post(
        "/items",
        json={"name": "123"}
    )
    response = client.patch(
        "/items/1",
        json={}
    )
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "123"}

def test_update_item_not_found(client):
    response = client.patch(
        "/items/999",
        json={}
    )
    assert response.status_code == 404

def test_delete_item(client):
    client.post(
        "/items",
        json={"name": "123"}
    )
    response = client.delete(
        "/items/1"
    )
    assert response.status_code == 204
    response = client.get(
        "/items/1"
    )
    assert response.status_code == 404

def test_delete_item_not_found(client):
    response = client.delete(
        "/items/999"
    )
    assert response.status_code == 404

def test_create_item_invalid_body(client):
    response = client.post(
        "/items",
        json={}
    )
    assert response.status_code == 422

def test_get_item_invalid_id(client):
    response = client.get(
        "/items/abc"
    )
    assert response.status_code == 422