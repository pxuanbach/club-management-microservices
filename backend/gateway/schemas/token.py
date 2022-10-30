from typing import Optional
import uuid
from pydantic import BaseModel


class Token(BaseModel):
    token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True

class TokenPayload(BaseModel):
    id: Optional[uuid.UUID]