from fastapi import Depends, status, Response
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi import HTTPException

from deps.db import get_async_session
from auth import verify_access_token
from crud import CRUD
from config import settings
from models import Users


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_PATH}/auth/token",
)
crud = CRUD()


async def get_current_user(
    db: AsyncSession = Depends(get_async_session), token: str = Depends(reusable_oauth2)
) -> Users:
    token_payload = await verify_access_token(token)
    user = await crud.get(db, id=token_payload.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tiêu chí xác thực không hợp lệ.",
        )
    return user


def get_current_active_user(
    current_user: Users = Depends(get_current_user),
) -> Users:
    if not crud.is_active(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tài khoản bị đình chỉ.",
        )
    return current_user


def get_current_superuser(
    current_user: Users = Depends(get_current_user),
) -> Users:
    if not crud.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Tài khoản không đủ quyền.",
        )
    return current_user
    