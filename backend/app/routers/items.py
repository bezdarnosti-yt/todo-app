### app/routers/items.py

from fastapi import APIRouter, HTTPException, status
from app.services.items import items_service
from app.schemas.items import Item, ItemCreate, ItemUpdate, SearchResponse
from app.services.exceptions import ItemNotFoundError


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/search")
def search_item(q: str, limit: int = 10) -> SearchResponse:
    return items_service.search(q=q, limit=limit)

@router.get("")
def list_items() -> list[Item]:
    return items_service.list_items()
    
@router.post("", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate) -> Item:
    return items_service.create_item(data = item)
    
@router.get("/{item_id}")
def get_by_id(item_id: int) -> Item:
    try:
        return items_service.get_by_id(item_id = item_id)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")
    
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    try:
        items_service.delete_item(item_id = item_id)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")
    
@router.patch("/{item_id}", status_code=status.HTTP_200_OK)
def update_item(item_id: int, update: ItemUpdate) -> Item:
    try:
        return items_service.update_item(item_id = item_id, data = update)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")

