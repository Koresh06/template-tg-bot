from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import User


async def add_user(tg_id: int, username: str, session: AsyncSession) -> str:
    session.add(User(tg_id=tg_id, username=username))
    return True


async def query_users(session: AsyncSession) -> list[User]:
    username = await session.scalars(select(User.username))
    return username.all()