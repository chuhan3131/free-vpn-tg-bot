import random
import asyncio
import aiohttp
import aiofiles
from datetime import datetime
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types, Router

from utils.logger import logger
from config import BOT_TOKEN, KEYS_COUNTER, PUBLIC_KEY
from utils.services import counter_lock, read_keys_count, write_keys_count, make_request

router = Router()
dp = Dispatcher()


@router.message(Command("start"))
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


@router.message(Command("vpn"))
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
                f"<b>config:\n</b><code>{config_url}</code>\n\n"
                f"<b>valid until:</b> {date}\n"
                f"<b>traffic:</b> {traffic} GB\n\n"
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


@router.message(Command("donate"))
async def donate_cmd(message: types.Message):
    donate_text = (
        "<b>cryptobot:</b> t.me/send?start=IVehn3KCVlGR\n"
        "<b>ton:</b> <code>UQDVvTFlRLsQE0dS6JFrFgG8Gpx2YpN3F1IbilUold6T69cz</code>\n"
        "<b>usdt trc20:</b> <code>TKJ2K9kwfgAUngr5dPxt192NCoiQRGT9uF</code>"
    )

    await message.answer(donate_text, parse_mode="HTML", disable_web_page_preview=True)


@router.message(Command("api"))
async def donate_cmd(message: types.Message):
    api_text = (
    'the bot uses a public API to provide VPN configs, which can stop at any time :)\n\n'
    '**examples of use:**\n'
    '```\n'
    'curl -X POST "https://vpn-telegram.com/api/v1/key-activate/free-key" -H "Content-Type: application/json" -d \'{\n'
    '    "public_key": "b7a92b4cd1a2ced29e06059c61f624be",\n'
    '    "user_tg_id": 123456789\n'
    '  }\'\n'
    '```\n'
    '```python\n'
    'import requests\n\n'
    'response = requests.post(\n'
    '    "https://vpn-telegram.com/api/v1/key-activate/free-key",\n'
    '    json={\n'
    '        "public_key": "b7a92b4cd1a2ced29e06059c61f624be",\n'
    '        "user_tg_id": 123456789\n'
    '    }\n'
    ')\n'
    'print(response.json())\n'
    '```\n\n'
    '**response from the server:**\n'
    '```json\n'
    '{\n'
    '  "result": true,\n'
    '  "data": {\n'
    '    "key": "74aeff4d-6359-46b9-9a1c-8a1a020bad9f",\n'
    '    "config_url": "https://vpn-telegram.com/config/74aeff4d-6359-46b9-9a1c-8a1a020bad9f",\n'
    '    "traffic_limit": "5368709120", # byte limit\n'
    '    "traffic_limit_gb": 5,\n'
    '    "finish_at": "1767214800", # unix timestamp\n'
    '    "activated_at": null,\n'
    '    "status": "1",\n'
    '    "status_text": "Активирован",\n'
    '    "is_free": true\n'
    '  }\n'
    '}\n'
    '```'
    )

    await message.answer(api_text, parse_mode="Markdown")


@router.message()
async def any_message(message: types.Message):
    await message.answer(
        "use the following commands:\n\n" "/vpn - get a key\n" "/donate - for donations"
    )


def common_handlers(dp):
    dp.include_router(router)
