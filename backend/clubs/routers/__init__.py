from fastapi import APIRouter

from config import settings
from routers import clubs, event


router = APIRouter(prefix=settings.API_PATH)


router.include_router(clubs.router, tags=["clubs"])
router.include_router(event.router, tags=["event"])
