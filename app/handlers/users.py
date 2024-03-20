from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.requests import RequestsRepo


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, repo: RequestsRepo) -> None:
    user = await repo.users.check_user(message.from_user.id)

    if user:
        await repo.users.add_user(message.from_user.id, message.from_user.full_name)
        await message.answer(f'Привет, {message.from_user.full_name}!')
        await repo.session.commit()
    else:
        await message.answer('Вы уже зарегистрированы!')
