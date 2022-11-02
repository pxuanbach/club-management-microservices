from sqlalchemy.ext.asyncio import AsyncSession

from model import Users


class CRUDUser():
    async def get_user_by_username(self, db: AsyncSession, username: str) -> Users:
        return None

