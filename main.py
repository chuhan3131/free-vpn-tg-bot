import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from utils.handlers import setup_handlers

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    setup_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
