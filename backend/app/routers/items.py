### app/routers/items.py

from fastapi import APIRouter, HTTPException, status, Depends
from app.services.items import ItemsService
from app.schemas.items import Item, ItemCreate, ItemUpdate, SearchResponse
from app.services.exceptions import ItemNotFoundError
from app.dependencies import get_items_service


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/search")
def search_item(
    q: str,
    limit: int = 10,
    service: ItemsService = Depends(get_items_service)
) -> SearchResponse:
    return service.search(q=q, limit=limit)

@router.get("")
def list_items(
    service: ItemsService = Depends(get_items_service)
) -> list[Item]:
    return service.list_items()
    
@router.post("",status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    service: ItemsService = Depends(get_items_service),
) -> Item:
    return service.create_item(data = item)
    
@router.get("/{item_id}")
def get_by_id(
    item_id: int,
    service: ItemsService = Depends(get_items_service)
) -> Item:
    try:
        return service.get_by_id(item_id = item_id)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")
    
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    service: ItemsService = Depends(get_items_service)
) -> None:
    try:
        service.delete_item(item_id = item_id)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")
    
@router.patch("/{item_id}", status_code=status.HTTP_200_OK)
def update_item(
    item_id: int,
    update: ItemUpdate,
    service: ItemsService = Depends(get_items_service)
) -> Item:
    try:
        return service.update_item(item_id = item_id, data = update)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")

