from typing import Any, List
import uuid
from fastapi import APIRouter, status, Depends, HTTPException, UploadFile, File, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from constants import event_type_constants
from utils import upload_file
from crud import CRUD
from deps.db import get_async_session
from deps.user import get_current_active_user, get_current_superuser
from deps.request_params import parse_common_params
from models import Users
from schemas import User as UserSchema, UserCreate, UserUpdate, RequestParams
from event_handler import send_event


router = APIRouter(prefix="/users")
crud = CRUD()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=List[UserSchema],
)
async def get_users(
    request_params: RequestParams = Depends(parse_common_params(Users)),
    session: AsyncSession = Depends(get_async_session),
    # user: Users = Depends(get_current_superuser),
) -> Any:
    """
    Superuser get all users
    """
    users = await crud.get_multi(session, request_params)
    return users


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSchema,
)
async def create_user(
    background_task: BackgroundTasks,
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
    background_task.add_task(
        send_event,
        url=settings.EVENT_BUS_URL,
        event_type=event_type_constants.USER_CREATED,
        data={"id": str(user.id)} 
    )
    return user


@router.get(
    "/me",
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
    "/{user_id}", 
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


@router.patch(
    "/me",
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
    "/{user_id}",
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
    "/me/avatar",
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
    "/{user_id}",
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
    