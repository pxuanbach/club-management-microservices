from fastapi import Depends, status, Response, Request, Header
from jose import jwt
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi import HTTPException

from deps.db import get_async_session
from crud import CRUD
from config import settings
from models import Users


crud = CRUD()


async def get_current_user(
    session: AsyncSession = Depends(get_async_session), request_user_id: str = Header(None)
) -> Users:
    user = await crud.get(session, request_user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tiêu chí xác thực không hợp lệ.",
        )
    return user


async def get_current_active_user(
    current_user: Users = Depends(get_current_user),
) -> Users:
    if not crud.is_active(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tài khoản bị đình chỉ.",
        )
    return current_user


async def get_current_superuser(
    current_user: Users = Depends(get_current_user),
) -> Users:
    if not crud.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tài khoản không đủ quyền.",
        )
    return current_user
    