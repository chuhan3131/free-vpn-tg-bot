from datetime import datetime
import uuid
import random
import asyncio
from aiogram import Router
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from utils.logger import logger
from handlers.texts import get_text
from utils.files import counter_lock, get_banned_users, get_keys_count, write_keys_count
from utils.api import get_key, check_key
from config import DATA_FILE

router = Router()


@router.inline_query()
async def inline_vpn_handler(inline_query: InlineQuery):
    lang_code = inline_query.from_user.language_code
    query_text = inline_query.query.strip() 

    user_id = inline_query.from_user.id
    banned_users = await get_banned_users(DATA_FILE)

    if user_id in banned_users:
        banned_result = InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="faq",
            description="faq",
            input_message_content=InputTextMessageContent(
                message_text="faq",
                parse_mode="HTML",
            ),
        )
        await inline_query.answer([banned_result], cache_time=1)
        return

    try:
        if query_text.startswith("https://vpn-telegram.com/config/"):
            result_data = await check_key(query_text)

            if result_data["used_gb"] is None:
                title = get_text(lang_code, 'inline_check_title')
                description = get_text(lang_code, 'inline_check_error_description')
                text = get_text(lang_code, "error", error_msg="failed to verify key")
            else:
                traffic = result_data['used_gb']
                left = max(0, 5 - traffic)
                expires = result_data['expires']
                
                title = get_text(lang_code, 'inline_check_title')
                description = get_text(lang_code, 'inline_check_description')
                text = get_text(lang_code, 'check',
                    traffic=traffic, 
                    left=left, 
                    expires=expires
                )

            result = InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=title,
                description=description,
                input_message_content=InputTextMessageContent(
                    message_text=text,
                    parse_mode="HTML",
                ),
            )
            
            await inline_query.answer([result], cache_time=1)
            return

        user_id_for_api = random.randint(100_000_000, 999_999_999)
        response_data = await get_key(user_id_for_api)

        if response_data.get("result"):
            timestamp = response_data["data"]["finish_at"]
            dt = datetime.fromtimestamp(timestamp)
            date = dt.strftime("%d.%m.%Y, %H:%M")

            vpn_key = response_data["data"]["key"]
            traffic = response_data["data"]["traffic_limit_gb"]
            config_url = f"https://vpn-telegram.com/config/{vpn_key}"

            key_text = get_text(
                lang_code, "key", config_url=config_url, date=date, traffic=traffic
            )

            result = InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=get_text(lang_code, "inline_get_title"),
                description=get_text(lang_code, "inline_get_description"),
                input_message_content=InputTextMessageContent(
                    message_text=key_text,
                    parse_mode="HTML",
                ),
            )

            async with counter_lock:
                current_keys = await get_keys_count(DATA_FILE)
                new_keys = current_keys + 1
                await write_keys_count(new_keys, DATA_FILE)

        else:
            error_msg = response_data.get("message", "unknown error")
            error_text = get_text(lang_code, "error", error_msg=error_msg)

            result = InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=get_text(lang_code, "inline_error_title"),
                description=get_text(lang_code, "inline_get_error_description"),
                input_message_content=InputTextMessageContent(
                    message_text=error_text,
                    parse_mode="HTML",
                ),
            )

    except asyncio.TimeoutError:
        error_text = get_text(lang_code, "error", error_msg="request timeout")
        result = InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=get_text(lang_code, "inline_error_title"),
            description=get_text(lang_code, "inline_get_error_description"),
            input_message_content=InputTextMessageContent(
                message_text=error_text,
                parse_mode="HTML",
            ),
        )
        logger.error("Inline query timeout")

    except Exception as e:
        logger.error(f"Inline query error: {e}")
        error_text = get_text(lang_code, "error", error_msg="internal server error")
        result = InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title=get_text(lang_code, "inline_error_title"),
            description=get_text(lang_code, "inline_get_error_description"),
            input_message_content=InputTextMessageContent(
                message_text=error_text,
                parse_mode="HTML",
            ),
        )

    await inline_query.answer([result], cache_time=1)