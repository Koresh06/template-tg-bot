import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from app.config_loader import load_config
from app.database.session import create_engine_db, create_sessionmaker
from app.middlewares.db_session import DbSessionMiddleware
from app.handlers.users import users


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Staring bot')
    
    config = load_config()
    engine = create_engine_db(config.db)
    sessionmaker = create_sessionmaker(engine)
    

    bot: Bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp: Dispatcher = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(sessionmaker=sessionmaker))
    dp.include_routers(
        users
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
        logger.info('Запуск бота')
    except KeyboardInterrupt as exxit:
        logger.info(f'Бот закрыт {exxit}')
