import io
import random
import asyncio
from PIL import Image
from datetime import datetime
from aiogram.filters import Command
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.texts import get_text
from captcha.image import ImageCaptcha
from handlers.states import CaptchaState
from utils.captcha import generate_captcha
from keyboards.instruction import instruction_kb
from config import DATA_FILE, ADMIN_ID, CHANNEL_ID
from utils.api import get_key, check_key, parse_key
from utils.logger import logger, check_subscription, send_logs
from utils.settings import (
    counter_lock,
    get_banned_users,
    get_keys_count,
    write_keys_count,
    add_user_to_banned,
    write_captcha_enabled,
    read_captcha_enabled,
)

router = Router()

captcha_store = {}


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    name = message.from_user.first_name or ""
    username = message.from_user.username

    user_id = message.from_user.id
    banned_users = await get_banned_users(DATA_FILE)

    keys = await get_keys_count(DATA_FILE)
    lang_code = message.from_user.language_code

    if user_id in banned_users:
        await message.answer("faq")
        await send_logs(message=message, log="attempt to launch the bot")
        return
    else:
        start_text = get_text(lang_code, "start", name=name, keys=keys)
        await message.answer(start_text, parse_mode="HTML")

        await send_logs(message=message, log="bot start")


@router.message(Command("vpn"))
async def vpn_cmd(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    lang_code = message.from_user.language_code or "en"

    banned_users = await get_banned_users(DATA_FILE)
    if user_id in banned_users:
        await message.answer("faq")
        return

    is_subscribed = await check_subscription(message.bot, user_id, CHANNEL_ID)
    if not is_subscribed:
        await message.answer("to continue, subscribe to the @chuhandev channel.")
        return

    captcha_enabled = await read_captcha_enabled()

    if captcha_enabled:
        image_bytes, captcha_text = await generate_captcha()
        captcha_store[user_id] = captcha_text

        await state.update_data(
            {
                "user_id": user_id,
                "lang_code": lang_code,
                "message_id": message.message_id,
            }
        )

        await state.set_state(CaptchaState.waiting_captcha)

        await message.answer_photo(
            photo=types.BufferedInputFile(image_bytes, filename="captcha.png"),
            caption="enter the text from the image to get the key:",
        )

        await send_logs(message=message, log="key request with captcha")
    else:
        await parse_key(message)


@router.message(CaptchaState.waiting_captcha)
async def check_captcha(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_input = message.text.strip().upper()

    correct_text = captcha_store.get(user_id)

    if not correct_text:
        await message.answer("the captcha is out of date, please use /vpn again")
        await state.clear()
        return

    if user_input == correct_text:
        if user_id in captcha_store:
            del captcha_store[user_id]

        await state.clear()

        await parse_key(message)
    else:
        if user_id in captcha_store:
            del captcha_store[user_id]

        await add_user_to_banned(user_id)
        await message.answer("incorrect captcha, u are blocked.")
        await state.clear()

        await message.bot.send_message(
            ADMIN_ID,
            f"user banned - failed captcha: {user_id} (@{message.from_user.username or 'no'})",
        )


@router.message(Command("donate"))
async def donate_cmd(message: types.Message):
    lang_code = message.from_user.language_code
    username = message.from_user.username
    user_id = message.from_user.id

    donate_text = (
        f"<b>{get_text(lang_code, 'donate')}:</b>\n\n"
        "<b>cryptobot:</b> t.me/send?start=IVehn3KCVlGR\n"
        "<b>ton:</b> <code>UQDVvTFlRLsQE0dS6JFrFgG8Gpx2YpN3F1IbilUold6T69cz</code>\n"
        "<b>usdt trc20:</b> <code>TKJ2K9kwfgAUngr5dPxt192NCoiQRGT9uF</code>"
    )

    await message.answer(donate_text, parse_mode="HTML", disable_web_page_preview=True)

    await send_logs(message=message, log="viewing donations")


@router.message(Command("api"))
async def api_cmd(message: types.Message):

    lang_code = message.from_user.language_code
    banned_users = await get_banned_users(DATA_FILE)
    username = message.from_user.username
    user_id = message.from_user.id

    if user_id in banned_users:
        await message.answer("faq")
        await send_logs(message=message, log="attempt to view API")
        return

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
    await send_logs(message=message, log="view API")


@router.message(Command("check"))
async def check_cmd(message: types.Message):
    user_id = message.from_user.id
    lang_code = message.from_user.language_code
    args = message.text.split(maxsplit=1)
    banned_users = await get_banned_users(DATA_FILE)

    if user_id in banned_users:
        await message.answer("faq")
        return

    if len(args) < 2:
        await message.answer(get_text(lang_code, "check_error"), parse_mode="HTML")
        return

    config_url = args[1]

    generation_text = get_text(lang_code, "checking")
    status_message = await message.answer(generation_text, parse_mode="HTML")

    result = await check_key(config_url)

    if result["used_gb"] is None or result["expires"] is None:
        await status_message.edit_text(
            get_text(lang_code, "check_failed"), parse_mode="HTML"
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

    await status_message.edit_text(check_text, parse_mode="HTML")


@router.message(Command("instruction"))
async def instruction_cmd(message: types.Message):
    user_id = message.from_user.id
    banned_users = await get_banned_users(DATA_FILE)

    name = message.from_user.first_name or "hey"
    lang_code = message.from_user.language_code

    if user_id in banned_users:
        await message.answer("faq")
        return

    instruction_text = get_text(lang_code, "instruction", name=name)
    await message.answer(instruction_text, reply_markup=instruction_kb)


@router.message()
async def any_message(message: types.Message):
    user_id = message.from_user.id
    lang_code = message.from_user.language_code
    banned_users = await get_banned_users(DATA_FILE)

    if user_id in banned_users:
        await message.answer("faq")
        return

    any_message_text = get_text(lang_code, "any_message")
    await message.answer(any_message_text)
