### app/repositories/items.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.items import Item as ItemModel
from app.schemas.items import ItemUpdate, ItemCreate


class ItemsRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all(self) -> list[ItemModel]:
        result = await self._session.execute(select(ItemModel))
        return list(result.scalars().all())

    async def get_by_id(self, item_id: int) -> ItemModel | None:
        result = await self._session.execute(
            select(ItemModel).where(ItemModel.id == item_id)
        )
        return result.scalar_one_or_none()

    async def create(self, data: ItemCreate) -> ItemModel:
        instance = ItemModel(name=data.name)
        self._session.add(instance)
        await self._session.commit()
        await self._session.refresh(instance)
        return instance

    async def update(self, item_id: int, data: ItemUpdate) -> ItemModel | None:
        item = await self.get_by_id(item_id=item_id)
        if item is None:
            return None
        update_dict = data.model_dump(exclude_unset=True)
        if not update_dict:
            return item
        for key, value in update_dict.items():
            setattr(item, key, value)
        await self._session.commit()
        await self._session.refresh(item)
        return item

    async def delete(self, item_id: int) -> bool:
        item = await self.get_by_id(item_id=item_id)
        if item is None:
            return False
        await self._session.delete(item)
        await self._session.commit()
        return True
