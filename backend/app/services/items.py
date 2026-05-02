### app/services/items.py

from app.models.items import Item as ItemModel
from app.schemas.items import ItemCreate, ItemUpdate, SearchResponse
from app.repositories.items import ItemsRepository
from app.services.exceptions import ItemNotFoundError


class ItemsService:
    def __init__(self, repository: ItemsRepository):
        self._repository = repository

    async def list_items(self) -> list[ItemModel]:
        return await self._repository.get_all()

    async def get_by_id(self, item_id: int) -> ItemModel:
        item = await self._repository.get_by_id(item_id=item_id)
        if item is None:
            raise ItemNotFoundError()
        return item

    async def create_item(self, data: ItemCreate) -> ItemModel:
        return await self._repository.create(data=data)

    async def update_item(self, item_id: int, data: ItemUpdate) -> ItemModel:
        item = await self._repository.update(item_id=item_id, data=data)
        if item is None:
            raise ItemNotFoundError()
        return item

    async def delete_item(self, item_id: int) -> None:
        success: bool = await self._repository.delete(item_id=item_id)
        if not success:
            raise ItemNotFoundError()
        
    async def search(self, q: str, limit: int = 10) -> SearchResponse:
        return SearchResponse(query=q, limit=limit, results=[])
        
