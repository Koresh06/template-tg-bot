from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.data_access import add_user, query_users


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession) -> None:
    user = await add_user(message.from_user.id, message.from_user.username, session)

    if user:
        await message.answer(f'Привет, {message.from_user.full_name}!')
        await session.commit()

@router.message(Command('users'))
async def cmd_users(message: Message, session: AsyncSession) -> None:
    users = await query_users(session)
    print(users)