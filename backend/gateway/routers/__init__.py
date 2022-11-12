from fastapi import APIRouter

from routers import auth, users, clubs


router = APIRouter(prefix="/api/v1")


router.include_router(auth.router, tags=["auth"])
router.include_router(users.router, tags=["users"])
router.include_router(clubs.router, tags=["clubs"])
