### app/main.py

from fastapi import FastAPI
from app.routers import items, health
from app.config import settings


app = FastAPI(title=settings.app_name)


app.include_router(health.router)
app.include_router(items.router)
