import json
import logging
from typing import Any, Optional, List, Union

import aiofiles
from aiogram import Bot, types
from aiogram.types import InlineQuery
from aiogram.exceptions import TelegramBadRequest
from utils.settings import read_subscription_check, read_logs_enabled, read_captcha_enabled

from config import CHANNEL_ID, ADMIN_ID, DATA_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)


async def check_subscription(bot: Bot, user_id: int, channel_id: str) -> bool:
    subscription_check_enabled = await read_subscription_check()
    if not subscription_check_enabled:
        return True

    try:
        chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

        valid_statuses = ["member", "administrator", "creator"]
        if chat_member.status in valid_statuses:
            return True
        elif chat_member.status == "restricted":
            return chat_member.is_member
        else:
            return False

    except TelegramBadRequest as e:
        if (
            "chat not found" in str(e).lower()
            or "bot is not a member" in str(e).lower()
        ):
            logger.warning(f"bot cannot check subscription to {channel_id}: {e}")
            return True
        logger.error(f"telegram error checking subscription: {e}")
        return True
    except Exception as e:
        logger.error(f"error checking subscription: {e}")
        return True


async def send_logs(
    message: types.Message = None, inline_query: InlineQuery = None, log: str = None
):
    logs_enabled = await read_logs_enabled()
    if not logs_enabled:
        return

        username_text = f"@{username}" if username else "not_found"
        log_message = f"[{context}] {log}, user_id={user_id}, username={username_text}"

        logger.info(f"{log_message} (logs disabled)")
        return

    if message:
        user_id = message.from_user.id
        username = message.from_user.username
        context = "message"
    elif inline_query:
        user_id = inline_query.from_user.id
        username = inline_query.from_user.username
        context = "inline"
    else:
        logger.error("send_logs called without message or inline_query")
        return

    username_text = f"@{username}" if username else "not_found"
    log_message = f"[{context}] {log}, user_id={user_id}, username={username_text}"

    logger.info(log_message)

    bot = None
    if message:
        bot = message.bot
    elif inline_query:
        bot = inline_query.bot

    if bot and ADMIN_ID:
        try:
            await bot.send_message(chat_id=ADMIN_ID, text=log_message)
        except Exception as e:
            logger.error(f"failed to send log to admin: {e}")
