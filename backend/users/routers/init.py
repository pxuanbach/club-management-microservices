from typing import Any
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, status, Header
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from constants import event_type_constants
from auth import get_password_hash
from crud import CRUD
from event_handler import send_event
from deps.db import get_async_session
from deps.user import get_current_superuser
from models import Users


router = APIRouter(prefix="/init")
crud = CRUD()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    # include_in_schema=False
)
async def create_user(
    background_task: BackgroundTasks,
    secret: str = Header(...),
    session: AsyncSession = Depends(get_async_session),
) -> Any:
    """
    Superuser init data
    """
    if secret != settings.SECRET_KEY:
        raise HTTPException(400, "Không thể khởi tạo dữ liệu.")
    admin = await crud.get_by_username(session, settings.ADMIN_USERNAME)
    if not admin:
        admin = Users(
            username=settings.ADMIN_USERNAME,
            email=f"{settings.ADMIN_USERNAME}@gmail.com",
            full_name=settings.ADMIN_USERNAME,
            hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
            is_active=True,
            is_superuser=True,
        )
        session.add(admin)
        await session.commit()
        print("Tạo tài khoản admin thành công.")
    background_task.add_task(
        send_event,
        url=settings.EVENT_BUS_URL,
        event_type=event_type_constants.ADMIN_EXISTED,
        data={"id": str(admin.id)} 
    )
    return "Khởi tạo dữ liệu ban đầu thành công."
