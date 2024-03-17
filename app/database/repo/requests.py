from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.user import UserRepo


@dataclass
class RequestsRepo:

    session: AsyncSession

    @property
    def users(self) -> UserRepo:
        
        return UserRepo(self.session)

   