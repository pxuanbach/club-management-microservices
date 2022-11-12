import aiohttp
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from crud import CRUD
from constants import event_type_constants
from config import settings
from schemas import EventData


router = APIRouter(prefix="/events")
crud = CRUD()


@router.post("")
async def events(
    event: EventData,
):
    """Receive events from event-bus"""
    if event.type == "":
        pass
    return