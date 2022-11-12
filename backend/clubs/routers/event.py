from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
import json

from crud import CRUD
from config import settings
from deps.db import get_async_session
from schemas import EventData
from constants import event_type_constants


router = APIRouter(prefix="/events")
crud = CRUD()


@router.post("")
async def events(
    event: EventData,
    background_task: BackgroundTasks,
    session: AsyncSession = Depends(get_async_session),
):
    """Receive events from event-bus"""
    crud = CRUD()
    try:
        event_data = json.loads(event.data)
        if event.type == event_type_constants.USER_CREATED:
            background_task.add_task(
                crud.user_created,
                db=session,
                data=event_data
            )
        elif event.type == event_type_constants.ADMIN_EXISTED:
            background_task.add_task(
                crud.admin_exist,
                db=session,
                data=event_data
            )
        return "OK"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))