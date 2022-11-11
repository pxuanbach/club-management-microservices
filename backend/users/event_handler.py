import aiohttp
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
import json

from crud import CRUD
from config import settings
from schemas import EventData


router = APIRouter(prefix="/events", tags=["event"])
crud = CRUD()


@router.post("")
async def events(
    event: EventData,
):
    """Receive events from event-bus"""
    if event.type == "":
        pass
    return



async def send_event(url, event_type, data):
    send_data = EventData(
        type=event_type,
        data=json.dumps(data)
    )
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.post(url, json=send_data.dict()) as resp:
            # print(send_data.dict())
            print(await resp.text())
