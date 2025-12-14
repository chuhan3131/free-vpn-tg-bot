import random
import asyncio
from datetime import datetime
from aiogram.filters import Command
from aiogram import types, Router

from utils.logger import logger
from handlers.texts import get_text
from utils.files import counter_lock, read_keys_count, write_keys_count
from utils.api import get_key, check_key

router = Router()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    name = message.from_user.first_name or ""
    keys = await read_keys_count()
    lang_code = message.from_user.language_code

    start_text = get_text(lang_code, "start", name=name, keys=keys)
    await message.answer(start_text, parse_mode="HTML")


@router.message(Command("vpn"))
async def vpn_cmd(message: types.Message):
    lang_code = message.from_user.language_code
    generation_text = get_text(lang_code, "generation")

    msg = await message.answer(generation_text)

    try:
        user_id = random.randint(100_000_000, 999_999_999)
        response_data = await get_key(user_id)

        if "error" in response_data:
            error_text = get_text(lang_code, "error", error_msg=response_data["error"])
            await msg.edit_text(error_text, parse_mode="HTML")
            return

        if response_data.get("result"):
            timestamp = response_data["data"]["finish_at"]
            dt = datetime.fromtimestamp(timestamp)

            date = dt.strftime("%d.%m.%Y, %H:%M")
            vpn_key = response_data["data"]["key"]
            traffic = response_data["data"]["traffic_limit_gb"]
            config_url = f"https://vpn-telegram.com/config/{vpn_key}"

            result_text = get_text(
                lang_code, "key", config_url=config_url, date=date, traffic=traffic
            )

            await msg.edit_text(result_text, parse_mode="HTML")

            async with counter_lock:
                current_keys = await read_keys_count()
                new_keys = current_keys + 1
                await write_keys_count(new_keys)

        else:
            error_msg = response_data.get("message", "unknown error")
            error_text = get_text(lang_code, "error", error_msg=error_msg)
            await msg.edit_text(error_text, parse_mode="HTML")

    except asyncio.TimeoutError:
        error_text = get_text(lang_code, "error", error_msg="request timeout")
        await msg.edit_text(error_text, parse_mode="HTML")
        logger.error("API request timeout")

    except Exception as e:
        error_text = get_text(lang_code, "error", error_msg=str(e))
        await msg.edit_text(error_text, parse_mode="HTML")
        logger.error(f"Unexpected error: {e}")


@router.message(Command("donate"))
async def donate_cmd(message: types.Message):
    lang_code = message.from_user.language_code

    donate_text = (
        f"<b>{get_text(lang_code, 'donate')}:</b>\n\n"
        "<b>cryptobot:</b> t.me/send?start=IVehn3KCVlGR\n"
        "<b>ton:</b> <code>UQDVvTFlRLsQE0dS6JFrFgG8Gpx2YpN3F1IbilUold6T69cz</code>\n"
        "<b>usdt trc20:</b> <code>TKJ2K9kwfgAUngr5dPxt192NCoiQRGT9uF</code>"
    )

    await message.answer(donate_text, parse_mode="HTML", disable_web_page_preview=True)


@router.message(Command("api"))
async def api_cmd(message: types.Message):
    lang_code = message.from_user.language_code

    api_text = (
        f"{get_text(lang_code, 'api_intro')}\n\n"
        f"**{get_text(lang_code, 'api_examples')}**\n"
        "```\n"
        'curl -X POST "https://vpn-telegram.com/api/v1/key-activate/free-key" -H "Content-Type: application/json" -d \'{\n'
        '    "public_key": "b7a92b4cd1a2ced29e06059c61f624be",\n'
        '    "user_tg_id": 123456789\n'
        "  }'\n"
        "```\n"
        "```python\n"
        "import requests\n\n"
        "response = requests.post(\n"
        '    "https://vpn-telegram.com/api/v1/key-activate/free-key",\n'
        "    json={\n"
        '        "public_key": "b7a92b4cd1a2ced29e06059c61f624be",\n'
        '        "user_tg_id": 123456789\n'
        "    }\n"
        ")\n"
        "print(response.json())\n"
        "```\n\n"
        f"**{get_text(lang_code, 'api_response')}**\n"
        "```json\n"
        "{\n"
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
        "  }\n"
        "}\n"
        "```"
    )

    await message.answer(api_text, parse_mode="Markdown")


@router.message(Command("check"))
async def check_cmd(message: types.Message):
    lang_code = message.from_user.language_code
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.answer(
            get_text(lang_code, "check_error"),
            parse_mode="HTML"
        )
        return

    config_url = args[1]

    generation_text = get_text(lang_code, "checking")
    status_message = await message.answer(
        generation_text,
        parse_mode="HTML"
    )

    result = await check_key(config_url)

    if result["used_gb"] is None or result["expires"] is None:
        await status_message.edit_text(
            get_text(lang_code, "check_failed"),
            parse_mode="HTML"
        )
        return

    traffic = result["used_gb"]
    left = max(0, 5 - traffic)
    expires = result["expires"]

    check_text = get_text(
        lang_code,
        "check",
        traffic=traffic,
        left=left,
        expires=expires,
    )

    await status_message.edit_text(
        check_text,
        parse_mode="HTML"
    )


@router.message()
async def any_message(message: types.Message):
    lang_code = message.from_user.language_code
    any_message_text = get_text(lang_code, "any_message")
    await message.answer(any_message_text)
