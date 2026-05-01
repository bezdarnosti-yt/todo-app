### app/schemas/items.py

from pydantic import BaseModel

class Item(BaseModel):
    item_id: int
    name: str


class ItemCreate(BaseModel):
    name: str


class ItemUpdate(BaseModel):
    name: str | None = None


class SearchResponse(BaseModel):
    query: str
    limit: int
    results: list[str]
    