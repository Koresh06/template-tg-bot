from typing import Optional

from sqlalchemy import func, select

from app.database.models.users import User
from app.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def add_user(
        self,
        tg_id: int,
        username: str,
    ):
        user = User(tg_id=tg_id, username=username)
        await self.session.add(user)

        return True
