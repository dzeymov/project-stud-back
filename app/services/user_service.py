from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


async def get_user(db: AsyncSession, user_id: int) -> User | None:
    return await db.get(User, user_id)


async def list_users(db: AsyncSession) -> list[User]:
    result = await db.scalars(select(User))
    return list(result)