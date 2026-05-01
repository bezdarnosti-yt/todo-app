### app/services/items.py

from app.schemas.items import Item, ItemCreate, ItemUpdate, SearchResponse
from app.repositories.items import ItemsRepository
from app.services.exceptions import ItemNotFoundError


class ItemsService:
    def __init__(self, repository: ItemsRepository):
        self._repository = repository

    def list_items(self) -> list[Item]:
        return self._repository.get_all()

    def get_by_id(self, item_id: int) -> Item:
        item = self._repository.get_by_id(item_id=item_id)
        if item is None:
            raise ItemNotFoundError()
        return item

    def create_item(self, data: ItemCreate) -> Item:
        return self._repository.create(data=data)

    def update_item(self, item_id: int, data: ItemUpdate) -> Item:
        item = self._repository.update(item_id=item_id, data=data)
        if item is None:
            raise ItemNotFoundError()
        return item

    def delete_item(self, item_id: int) -> None:
        success: bool = self._repository.delete(item_id=item_id)
        if not success:
            raise ItemNotFoundError()
        
    def search(self, q: str, limit: int = 10) -> SearchResponse:
        return SearchResponse(query=q, limit=limit, results=[])
        
