import random
import asyncio
import requests
import threading
from datetime import datetime
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

from config import BOT_TOKEN, KEYS_COUNTER


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
counter_lock = threading.Lock()


def read_keys_count():
    try:
        with open(KEYS_COUNTER, "r", encoding="utf-8") as f:
            content = f.read().strip()
        return int(content) if content.isdigit() else 0
    except (FileNotFoundError, ValueError):
        return 0


def write_keys_count(value):
    with open(KEYS_COUNTER, "w", encoding="utf-8") as f:
        f.write(str(value))


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    name = message.from_user.first_name or "friend"
    keys = read_keys_count()

    await message.answer(
        f"hi {name}\n\n"
        "/vpn - get a key\n"
        "/donate - for donations\n\n"
        f"in total the bot issued <code>{keys}</code> keys",
        parse_mode="HTML",
    )


@dp.message(Command("vpn"))
async def vpn_cmd(message: types.Message):
    msg = await message.answer("generating a key...")

    try:
        user_id = random.randint(100_000_000, 999_999_999)

        response = requests.post(
            "https://vpn-telegram.com/api/v1/key-activate/free-key",
            headers={"User-Agent": "chuhan/1.0"},
            json={
                "public_key": "b7a92b4cd1a2ced29e06059c61f624be",
                "user_tg_id": user_id,
            },
            timeout=10,
        )

        response_data = response.json()

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
            
            with counter_lock:
                current_keys = read_keys_count()
                new_keys = current_keys + 1
                write_keys_count(new_keys)

        else:
            await msg.edit_text(
                f"error: {response_data.get('message', 'unknown error')}"
            )

    except Exception as e:
        await msg.edit_text(f"error during generation: {str(e)}")


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
        "use the following commands:\n\n"
        "/vpn - get a key\n"
        "/donate - for donations"
    )


async def main():
    print("started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())