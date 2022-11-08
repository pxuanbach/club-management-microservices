from typing import Any, Dict, List, Optional, Union
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from fastapi.encoders import jsonable_encoder

from config import settings
from models import Clubs
from schemas import ClubCreate, ClubUpdate


class CRUD:
    async def get(self, db: AsyncSession, id: Any) -> Optional[Clubs]:
        return (
            (
                await db.execute(
                    select(Clubs)
                    .filter(Clubs.id == id)
                )
            )
            .scalars()
            .first()
        )

    async def get_multi(
        self, db: AsyncSession
    ) -> List[Clubs]:
        datas = (
            (
                await db.execute(
                    select(Clubs)
                )
            )
            .scalars()
            .all()
        )
        return datas

    async def create(self, db: AsyncSession, obj_in: ClubCreate) -> Clubs:
        create_data = obj_in.dict(exclude_unset=True)
        user = Clubs(
            **create_data,
        )
        db.add(user)
        await db.commit()
        return user

    async def update(
        self,
        db: AsyncSession,
        *,
        db_obj: Clubs,
        obj_in: Union[ClubUpdate, Dict[str, Any]]
    ) -> Clubs:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True, exclude_none=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        await db.commit()
        return db_obj

    async def delete(self, db: AsyncSession, *, id: Any) -> Clubs:
        # obj = await db.get(Clubs, id)
        # await db.delete(obj)
        # await db.commit()
        return 