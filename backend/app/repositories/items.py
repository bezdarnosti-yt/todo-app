### app/repositories/items.py

from app.schemas.items import Item, ItemCreate, ItemUpdate


class ItemsRepository:
    def __init__(self):
        self._items: list[Item] = []
        self._next_id: int = 1

    def get_all(self) -> list[Item]:
        return self._items

    def get_by_id(self, item_id: int) -> Item | None:
        for item in self._items:
            if item.item_id == item_id:
                return item
        return None

    def create(self, data: ItemCreate) -> Item:
        instance = Item(item_id=self._next_id, name=data.name)
        self._next_id += 1
        self._items.append(instance)
        return instance

    def update(self, item_id: int, data: ItemUpdate) -> Item | None:
        update_dict = data.model_dump(exclude_unset=True)
        for item in self._items:
            if item.item_id == item_id:
                for key, value in update_dict.items():
                    setattr(item, key, value)
                return item
        return None

    def delete(self, item_id: int) -> bool:
        for index, item in enumerate(self._items):
            if item.item_id == item_id:
                self._items.pop(index)
                return True
        return False

    
items_repository = ItemsRepository()
