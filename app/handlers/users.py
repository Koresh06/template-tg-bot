from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.data_access import add_username, query_users


users = Router()


@users.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession) -> None:
    username = await add_username(message.from_user.username, session)

    if username:
        await message.answer(f'Привет, {message.from_user.full_name}!')

@users.message(Command('users'))
async def cmd_users(message: Message, session: AsyncSession) -> None:
    users = await query_users(session)
    print(users)