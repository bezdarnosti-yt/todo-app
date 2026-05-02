### app/routers/items.py

from fastapi import APIRouter, HTTPException, status, Depends
from app.services.items import ItemsService
from app.schemas.items import Item as ItemSchema
from app.models.items import Item as ItemModel
from app.schemas.items import ItemCreate, ItemUpdate, SearchResponse
from app.services.exceptions import ItemNotFoundError
from app.dependencies import get_items_service


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/search")
async def search_item(
    q: str, limit: int = 10, service: ItemsService = Depends(get_items_service)
) -> SearchResponse:
    return await service.search(q=q, limit=limit)


@router.get("")
async def list_items(
    service: ItemsService = Depends(get_items_service),
) -> list[ItemSchema]:
    return await service.list_items()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_item(
    item: ItemCreate,
    service: ItemsService = Depends(get_items_service),
) -> ItemSchema:
    result: ItemModel = await service.create_item(data=item)
    return ItemSchema.model_validate(result)


@router.get("/{item_id}", response_model=ItemSchema)
async def get_by_id(
    item_id: int, service: ItemsService = Depends(get_items_service)
) -> ItemSchema:
    try:
        item: ItemModel = await service.get_by_id(item_id=item_id)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")
    return ItemSchema.model_validate(item)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: int, service: ItemsService = Depends(get_items_service)
) -> None:
    try:
        await service.delete_item(item_id=item_id)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")


@router.patch("/{item_id}", status_code=status.HTTP_200_OK, response_model=ItemSchema)
async def update_item(
    item_id: int, update: ItemUpdate, service: ItemsService = Depends(get_items_service)
) -> ItemSchema:
    try:
        item: ItemModel = await service.update_item(item_id=item_id, data=update)
    except ItemNotFoundError:
        raise HTTPException(404, "Item not found")
    return ItemSchema.model_validate(item)
