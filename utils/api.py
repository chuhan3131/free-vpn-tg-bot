import re
import io
import random
import aiohttp
import asyncio
from PIL import Image
from datetime import datetime
from bs4 import BeautifulSoup
from aiogram import types, Router, F
from aiogram.filters import Command
from captcha.image import ImageCaptcha
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from handlers.texts import get_text
from keyboards.instruction import instruction_kb
from config import DATA_FILE, ADMIN_ID, CHANNEL_ID, PUBLIC_KEY
from utils.logger import logger, check_subscription, send_logs
from utils.settings import (
    counter_lock,
    get_banned_users,
    get_keys_count,
    write_banned_users,
    write_keys_count,
)


async def get_key(user_id: int) -> dict:
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


async def check_key(config_url: str) -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0"
    }

    result = {"used_gb": None, "expires": None}

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(
                config_url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(f"API error {response.status}: {error_text}")
                    return result

                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                used_label = soup.find(
                    lambda tag: tag.name == "span" and "Использовано:" in tag.text
                )
                if used_label:
                    used_text = used_label.find_next("span").text.strip()
                    match = re.search(r"([\d.]+)", used_text)
                    if match:
                        result["used_gb"] = float(match.group(1))

                expires_label = soup.find(
                    lambda tag: tag.name == "span" and "Действует до:" in tag.text
                )
                if expires_label:
                    expires_value = expires_label.find_next("span").text.strip()
                    result["expires"] = expires_value

                return result

        except Exception as e:
            logger.error(f"Request failed: {e}")
            return result


async def parse_key(message: types.Message):
    lang_code = message.from_user.language_code or "en"
    generation_text = get_text(lang_code, "generation")
    username = message.from_user.username
    user_id = message.from_user.id

    msg = await message.answer(generation_text)

    try:
        user_id_for_api = random.randint(100_000_000, 999_999_999)
        response_data = await get_key(user_id_for_api)

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
            await send_logs(message=message, log="key sent")

            async with counter_lock:
                current_keys = await get_keys_count(DATA_FILE)
                new_keys = current_keys + 1
                await write_keys_count(new_keys, DATA_FILE)

        else:
            error_msg = response_data.get("message", "unknown error")
            error_text = get_text(lang_code, "error", error_msg=error_msg)
            await msg.edit_text(error_text, parse_mode="HTML")
            await send_logs(message=message, log=f"{error_text}")

    except asyncio.TimeoutError:
        error_text = get_text(lang_code, "error", error_msg="request timeout")
        await msg.edit_text(error_text, parse_mode="HTML")
        await send_logs(message=message, log=f"{error_text}")

    except Exception as e:
        error_text = get_text(lang_code, "error", error_msg=str(e))
        await msg.edit_text(error_text, parse_mode="HTML")
        await send_logs(message=message, log=f"{error_text}")
