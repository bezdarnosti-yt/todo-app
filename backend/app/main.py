### app/main.py

from fastapi import FastAPI
from app.routers import items, health
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(items.router)
