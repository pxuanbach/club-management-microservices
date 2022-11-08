from typing import Optional
import uuid
from pydantic import BaseModel


class ClubCreate(BaseModel):
    name: str
    description: Optional[str] = None
    leader: uuid.UUID
    is_blocked: Optional[bool] = None
    img_url: Optional[str] = None


class ClubUpdate(ClubCreate):
    name: Optional[str] = None
    leader: Optional[str] = None


class Club(ClubCreate):
    id: uuid.UUID

    class Config:
        orm_mode = True