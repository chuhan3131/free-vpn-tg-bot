import random
import asyncio
import aiohttp
import aiofiles
from datetime import datetime
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

from config import BOT_TOKEN, KEYS_COUNTER, PUBLIC_KEY


counter_lock = asyncio.Lock()


async def read_keys_count() -> int:
    try:
        async with aiofiles.open(KEYS_COUNTER, "r", encoding="utf-8") as f:
            content = (await f.read()).strip()
        return int(content) if content.isdigit() else 0
    except FileNotFoundError:
        async with aiofiles.open(KEYS_COUNTER, "w", encoding="utf-8") as f:
            await f.write("0")
        return 0
    except ValueError:
        return 0


async def write_keys_count(value: int) -> None:
    async with aiofiles.open(KEYS_COUNTER, "w", encoding="utf-8") as f:
        await f.write(str(value))


async def make_request(user_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        json_data = {
            "public_key": PUBLIC_KEY,
            "user_tg_id": user_id,
        }

        headers = {"User-Agent": "chuhan/1.0"}

        async with session.post(
            "https://vpn-telegram.com/api/v1/key-activate/free-key",
            headers=headers,
            json=json_data,
            timeout=aiohttp.ClientTimeout(total=10),
        ) as response:

            if response.status != 200:
                error_text = await response.text()
                logger.error(f"API error {response.status}: {error_text}")
                return {"error": f"API error: {response.status}"}

            return await response.json()
