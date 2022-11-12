from typing import Optional
import uuid
from pydantic import BaseModel


class Club(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str] = None
    leader: uuid.UUID
    is_blocked: Optional[bool] = False
    img_url: Optional[str] = None

    class Config:
        orm_mode = True