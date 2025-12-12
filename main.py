import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.common import common_handlers
from handlers.inline import router as inline_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    common_handlers(dp)
    dp.include_router(inline_router)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())