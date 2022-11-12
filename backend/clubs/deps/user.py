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
    user = await crud.get_user_by_id(session, request_user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tiêu chí xác thực không hợp lệ.",
        )
    return user
    