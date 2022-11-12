from typing import Optional, Literal
import uuid
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: Optional[uuid.UUID] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None
    description: Optional[str] = None
    gender: Optional[Literal["Nam", "Nữ", "Khác"]] = None
    phone: Optional[str] = None
    img_url: Optional[str] = None

    class Config:
        orm_mode = True