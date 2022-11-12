from datetime import timedelta
from typing import Any
from fastapi import APIRouter, Form, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from crud import CRUD
from auth import create_access_token, verify_access_token
from deps.db import get_async_session
from models import Users
from schemas import User as UserSchema, Token


router = APIRouter(prefix="/auth")
crud = CRUD()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_async_session)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user_in_db: Users = await crud.authenticate(
        session, form_data.username, form_data.password
    )
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tiêu chí xác thực không hợp lệ.',
        )
    token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        user_in_db.username, 
        user_in_db.id, 
        user_in_db.is_superuser, 
        expires_delta=token_expires
    )
    return Token(token=token)


@router.post(
    "/token",
    status_code=status.HTTP_200_OK,
    include_in_schema=False
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_async_session)
) -> Any:
    """
    Authorize in Swagger UI
    """
    user_in_db: Users = await crud.authenticate(session, form_data.username, form_data.password)
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tiêu chí xác thực không hợp lệ.',
        )
    token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(
        user_in_db.username, 
        user_in_db.id, 
        user_in_db.is_superuser,
        expires_delta=token_expires
    )
    return {"access_token": token, "token_type": "bearer"}


@router.post(
    "/verify-token",
    status_code=status.HTTP_200_OK,
    response_model=UserSchema
)
async def verify_token(
    token: str = Form(...),
    session: AsyncSession = Depends(get_async_session),
) -> Any:
    """
    Verify token
    """
    payload = await verify_access_token(token)
    user = await crud.get(session, payload.id)
    if not user:
        raise HTTPException(404, detail="Tiêu chí xác thực không hợp lệ.")
    return user
