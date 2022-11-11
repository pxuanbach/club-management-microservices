import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID

from db import Base


class Clubs(Base):
    __tablename__ = "clubs"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    img_url = Column(Text)
    description = Column(String)
    leader = Column(UUID(as_uuid=True))
    is_blocked = Column(Boolean, default=False)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
