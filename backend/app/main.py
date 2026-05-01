### app/main.py

from fastapi import FastAPI
from app.routers import items, health


app = FastAPI()


app.include_router(health.router)
app.include_router(items.router)
