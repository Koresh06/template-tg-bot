from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User


async def add_username(username: str, session: AsyncSession) -> str:
    async with session() as db_session:
        db_session.add(User(username=username))
        await session.commit()
        return True


async def query_users(session: AsyncSession) -> list[User]:
    async with session() as db_session:
        username = await db_session.execute(select(User.username))
    return username