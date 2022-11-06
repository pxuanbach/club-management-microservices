from typing import Any, Dict, List, Optional, Union
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from fastapi.encoders import jsonable_encoder

from config import settings
from auth import verify_password, get_password_hash
from models import Users
from schemas import UserCreate, UserUpdate


class CRUDUser():
    async def get_by_username(
        self, db: AsyncSession, username: str
    ) -> Optional[Users]:
        user = (
            (
                await db.execute(
                    select(Users)
                    .where(Users.username == username)
                )
            )
            .scalars()
            .first()
        )
        return user

    async def get(self, db: AsyncSession, id: Any) -> Optional[Users]:
        return (
            (
                await db.execute(
                    select(Users)
                    .filter(Users.id == id)
                )
            )
            .scalars()
            .first()
        )

    async def get_multi(
        self, db: AsyncSession
    ) -> List[Users]:
        datas = (
            (
                await db.execute(
                    select(Users)
                    .where(Users.username != settings.ADMIN_USERNAME)
                )
            )
            .scalars()
            .all()
        )
        return datas

    async def create(self, db: AsyncSession, *, obj_in: UserCreate) -> Users:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Users(**obj_in_data)  # type: ignore
        db.add(db_obj)
        await db.commit()
        return db_obj

    async def update(
        self,
        db: AsyncSession,
        *,
        db_obj: Users,
        obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> Users:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        return db_obj

    async def delete(self, db: AsyncSession, *, id: Any) -> Users:
        obj = await db.get(Users, id)
        await db.delete(obj)
        await db.commit()
        return 

    async def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[Users]:
        user = await self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: Users) -> bool:
        return user.is_active

    def is_superuser(self, user: Users) -> bool:
        return user.is_superuser

    async def change_password(self, db: AsyncSession, user: Users, new_password: str) -> None:
        hashed_password = get_password_hash(new_password)
        user.hashed_password = hashed_password
        db.add(user)
        await db.commit()
