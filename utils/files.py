import aiofiles
import asyncio
from datetime import datetime

from config import KEYS_COUNTER


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