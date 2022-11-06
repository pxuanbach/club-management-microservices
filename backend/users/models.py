import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

from db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    description = Column(String(255), nullable=True)
    gender = Column(String(10), default="Khác", comment="Nam/Nữ/Khác")
    phone = Column(String(12), nullable=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
