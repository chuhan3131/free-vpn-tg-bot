import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.user_handlers import router as user_router
from handlers.inline import router as inline_router
from handlers.callbacks import router as callbacks_router
from handlers.admin_handlers import router as admin_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(admin_router)
    dp.include_router(callbacks_router)
    dp.include_router(user_router)
    dp.include_router(inline_router)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
