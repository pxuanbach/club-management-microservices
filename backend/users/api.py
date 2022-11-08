from datetime import timedelta
import json
from typing import Any, List
import uuid
from fastapi import APIRouter, status, Depends, HTTPException, Body, UploadFile, File
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from utils import upload_file
from crud import CRUD
from auth import verify_password, get_password_hash, create_access_token
from deps.db import get_async_session
from deps.user import get_current_active_user, get_current_superuser
from models import Users
from schemas import User as UserSchema, UserCreate, UserUpdate, Token


router = APIRouter(prefix=settings.API_PATH)
crud = CRUD()


@router.post(
    "/auth/login",
    status_code=status.HTTP_200_OK,
    tags=["auth"]
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
        get_password_hash("ádasdkasdn")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tiêu chí xác thực không hợp lệ.',
        )
    token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user_in_db.username, user_in_db.id, expires_delta=token_expires)
    return Token(token=token)


@router.post(
    "/auth/token",
    status_code=status.HTTP_200_OK,
    tags=["auth"],
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
        get_password_hash("ádasdkasdn")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tiêu chí xác thực không hợp lệ.',
        )
    token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user_in_db.username, user_in_db.id, expires_delta=token_expires)
    return {"access_token": token, "token_type": "bearer"}


@router.post(
    "/auth/verify-token",
    status_code=status.HTTP_200_OK,
    tags=["auth"],
    response_model=UserSchema
)
async def verify_token(
    token: str = Body(...),
    session: AsyncSession = Depends(get_async_session),
) -> Any:
    """
    Verify token
    """
    return 


@router.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=List[UserSchema],
)
async def get_users(
    # request_params: RequestParams = Depends(parse_common_params(Users)),
    session: AsyncSession = Depends(get_async_session),
    # user: Users = Depends(get_current_superuser),
) -> Any:
    """
    Superuser get all users
    """
    users = await crud.get_multi(session)
    return users


@router.get(
    "/users/me",
    status_code=status.HTTP_200_OK,
    response_model=UserSchema
)
async def get_me(
    user: Users = Depends(get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return user



@router.get(
    "/users/{user_id}", 
    status_code=status.HTTP_200_OK,
    response_model=UserSchema
)
async def get_user_by_id(
    user_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    current_user: Users = Depends(get_current_superuser),
) -> Any:
    """
    Get a specific user by id.
    Just superuser or own user.
    """
    user = await crud.get(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Người dùng không tồn tại.",
        )
    return user


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSchema,
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_async_session),
    user: Users = Depends(get_current_superuser),
) -> Any:
    """
    Superuser create user
    """
    user = await crud.get_by_username(session, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tài khoản đã tồn tại.",
        )
    user = await crud.create(session, obj_in=user_in)
    return user


@router.patch(
    "/users/me",
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
)
async def update_user_by_id(
    user_in: UserUpdate,
    session: AsyncSession = Depends(get_async_session),
    current_user: Users = Depends(get_current_active_user),
) -> Any:
    """
    Update a specific user by id.
    Just superuser.
    """
    user = await crud.get(session, current_user.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Người dùng không tồn tại.",
        )
    user = await crud.update(session, db_obj=user, obj_in=user_in)
    return user


@router.patch(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
)
async def update_user_by_id(
    user_id: uuid.UUID,
    user_in: UserUpdate,
    session: AsyncSession = Depends(get_async_session),
    current_user: Users = Depends(get_current_superuser),
) -> Any:
    """
    Update a specific user by id.
    """
    user = await crud.get(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Người dùng không tồn tại.",
        )
    user = await crud.update(session, db_obj=user, obj_in=user_in)
    return user


@router.patch(
    "/users/me/avatar",
    status_code=status.HTTP_200_OK,
    response_model=UserSchema,
)
async def update_user_avatar(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_async_session),
    current_user: Users = Depends(get_current_active_user),
) -> Any:
    user = await crud.get(session, current_user.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Người dùng không tồn tại.",
        )
    img_url = await upload_file(file)
    user = await crud.update(session, db_obj=user, obj_in=UserUpdate(img_url=img_url))
    return user


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_user_by_id(
    user_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    current_user: Users = Depends(get_current_superuser),
) -> Any:
    user = await crud.get(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Người dùng không tồn tại.",
        )
    await crud.delete(session, id=user_id)
    return "Xóa người dùng thành công."
    