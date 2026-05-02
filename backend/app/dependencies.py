### app/dependencies.py

from fastapi import Depends
from app.repositories.items import ItemsRepository
from app.services.items import ItemsService
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_items_repository(
        session: AsyncSession = Depends(get_session)
) -> ItemsRepository:
    return ItemsRepository(session)

def get_items_service(repository: ItemsRepository = Depends(get_items_repository)) -> ItemsService:
    return ItemsService(repository=repository)