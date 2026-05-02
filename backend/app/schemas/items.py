### app/schemas/items.py

from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    name: str

class ItemUpdate(BaseModel):
    name: str | None = None

class Item(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class SearchResponse(BaseModel):
    query: str
    limit: int
    results: list[str]
    