import aiohttp
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
import json

from crud import CRUD
from config import settings
from deps.db import get_async_session
from schemas import EventData
from constants import event_type_constants


router = APIRouter(prefix="/events", tags=["event"])
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
        return "OK"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def send_event(url, event_type, data):
    send_data = EventData(
        type=event_type,
        data=json.dumps(data)
    )
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(url, json=send_data.dict()) as resp:
            print(resp.status)
            print(await resp.text())
