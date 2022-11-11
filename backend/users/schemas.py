from datetime import datetime
from typing import Optional, Literal, Any
import uuid
from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    full_name: Optional[str] = None
    description: Optional[str] = None
    gender: Optional[Literal["Nam", "Nữ", "Khác"]] = None
    phone: Optional[str] = None
    img_url: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    username: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class Token(BaseModel):
    token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True

class TokenPayload(BaseModel):
    id: Optional[uuid.UUID]


class EventData(BaseModel):
    type: str
    data: Optional[Any]
    