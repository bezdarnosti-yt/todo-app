### app/dependencies.py

from fastapi import Depends
from app.repositories.items import ItemsRepository, items_repository
from app.services.items import ItemsService


def get_items_repository() -> ItemsRepository:
    return items_repository

def get_items_service(repository: ItemsRepository = Depends(get_items_repository)) -> ItemsService:
    return ItemsService(repository=repository)