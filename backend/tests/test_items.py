### tests/test_items.py


async def test_health_check(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


async def test_create_item(client):
    response = await client.post("/items", json={"name": "test"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "test"}

    list_response = await client.get("/items")
    assert list_response.json() == [{"id": 1, "name": "test"}]


async def test_list_items_empty(client):
    response = await client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


async def test_list_items_after_create(client):
    await client.post("/items", json={"name": "123"})
    await client.post("/items", json={"name": "456"})
    response = await client.get("/items")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "123"}, {"id": 2, "name": "456"}]


async def test_get_item_by_id(client):
    await client.post("/items", json={"name": "123"})
    response = await client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "123"}


async def test_get_item_not_found(client):
    response = await client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


async def test_update_item(client):
    await client.post("/items", json={"name": "123"})
    response = await client.patch("/items/1", json={"name": "new"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "new"}


async def test_update_item_partial(client):
    await client.post("/items", json={"name": "123"})
    response = await client.patch("/items/1", json={})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "123"}


async def test_update_item_not_found(client):
    response = await client.patch("/items/999", json={})
    assert response.status_code == 404


async def test_delete_item(client):
    await client.post("/items", json={"name": "123"})
    response = await client.delete("/items/1")
    assert response.status_code == 204
    response = await client.get("/items/1")
    assert response.status_code == 404


async def test_delete_item_not_found(client):
    response = await client.delete("/items/999")
    assert response.status_code == 404


async def test_create_item_invalid_body(client):
    response = await client.post("/items", json={})
    assert response.status_code == 422


async def test_get_item_invalid_id(client):
    response = await client.get("/items/abc")
    assert response.status_code == 422
