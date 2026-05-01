### app/routers/health.py

from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok"}