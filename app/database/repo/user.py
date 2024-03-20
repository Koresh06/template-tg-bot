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
        self.session.add(user)

        return True

    async def check_user(self, tg_id: int) -> Optional[User]:
        user = await self.session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            return True
        return False