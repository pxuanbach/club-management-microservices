from fastapi import APIRouter

from config import settings
from routers import auth, users, event, init


router = APIRouter(prefix=settings.API_PATH)


router.include_router(init.router, tags=["init"])
router.include_router(auth.router, tags=["auth"])
router.include_router(users.router, tags=["users"])
router.include_router(event.router, tags=["event"])
