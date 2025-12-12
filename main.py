import random
import asyncio
import logging
import aiohttp
import aiofiles
from datetime import datetime
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

from config import BOT_TOKEN, KEYS_COUNTER, PUBLIC_KEY

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

counter_lock = asyncio.Lock()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


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


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    name = message.from_user.first_name or "friend"
    keys = await read_keys_count()

    await message.answer(
        f"hi {name}\n\n"
        "/vpn - get a key\n"
        "/donate - for donations\n\n"
        f"in total the bot issued <code>{keys}</code> keys",
        parse_mode="HTML",
    )


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


@dp.message(Command("vpn"))
async def vpn_cmd(message: types.Message):
    msg = await message.answer("generating a key...")

    try:
        user_id = random.randint(100_000_000, 999_999_999)

        response_data = await make_request(user_id)

        if "error" in response_data:
            await msg.edit_text(f"{response_data['error']}", parse_mode="HTML")
            return

        if response_data.get("result"):
            timestamp = response_data["data"]["finish_at"]
            dt = datetime.fromtimestamp(timestamp)

            date = dt.strftime("%-d %b %Y, %H:%M").lower()
            vpn_key = response_data["data"]["key"]
            traffic = response_data["data"]["traffic_limit_gb"]
            config_url = f"https://vpn-telegram.com/config/{vpn_key}"

            result_text = (
                f"<b>key generated!</b>\n\n"
                f"<b>config:</b> <code>{config_url}</code>\n"
                f"<b>valid until:</b> {date}\n"
                f"<b>traffic:</b> {traffic} gb\n\n"
                "by @chfreevpn_bot"
            )

            await msg.edit_text(result_text, parse_mode="HTML")

            async with counter_lock:
                current_keys = await read_keys_count()
                new_keys = current_keys + 1
                await write_keys_count(new_keys)

        else:
            error_msg = response_data.get("message", "unknown error")
            await msg.edit_text(f"error: <code>{error_msg}</code>", parse_mode="HTML")

    except asyncio.TimeoutError:
        await msg.edit_text("error: <code>request timeout</code>", parse_mode="HTML")
        logger.error("API request timeout")

    except aiohttp.ClientError as e:
        await msg.edit_text(f"error: <code>network error</code>", parse_mode="HTML")
        logger.error(f"Network error: {e}")

    except Exception as e:
        await msg.edit_text(
            f"error during generation: <code>{str(e)}</code>", parse_mode="HTML"
        )
        logger.error(f"Unexpected error: {e}")


@dp.message(Command("donate"))
async def donate_cmd(message: types.Message):
    donate_text = (
        "<b>cryptobot:</b> t.me/send?start=IVehn3KCVlGR\n"
        "<b>ton:</b> <code>UQDVvTFlRLsQE0dS6JFrFgG8Gpx2YpN3F1IbilUold6T69cz</code>\n"
        "<b>usdt trc20:</b> <code>TKJ2K9kwfgAUngr5dPxt192NCoiQRGT9uF</code>"
    )

    await message.answer(donate_text, parse_mode="HTML", disable_web_page_preview=True)


@dp.message()
async def any_message(message: types.Message):
    await message.answer(
        "use the following commands:\n\n" "/vpn - get a key\n" "/donate - for donations"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
