from datetime import datetime
import uuid
import random

from aiogram import Router
from aiogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from config import KEYS_COUNTER
from utils.logger import logger
from utils.services import (
    counter_lock,
    read_keys_count,
    write_keys_count,
    make_request,
)

router = Router()


@router.inline_query()
async def inline_vpn_handler(inline_query: InlineQuery):
    user_id = random.randint(100_000_000, 999_999_999)
    response_data = await make_request(user_id)

    if response_data.get("result"):
        timestamp = response_data["data"]["finish_at"]
        dt = datetime.fromtimestamp(timestamp)
        date = dt.strftime("%-d %b %Y, %H:%M").lower()
        vpn_key = response_data["data"]["key"]
        traffic = response_data["data"]["traffic_limit_gb"]
        config_url = f"https://vpn-telegram.com/config/{vpn_key}"

        result = InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="get free vpn!",
            description="click to generate VPN configuration",
            input_message_content=InputTextMessageContent(
                message_text=(
                    f"<b>your config:</b>\n<code>{config_url}</code>\n\n"
                    f"<b>valid until:</b> {date}\n"
                    f"<b>traffic:</b> {traffic} GB"
                ),
                parse_mode="HTML",
            ),
        )

        async with counter_lock:
            current_keys = await read_keys_count()
            new_keys = current_keys + 1
            await write_keys_count(new_keys)

    else:
        result = InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="error",
            description="failed to generate VPN",
            input_message_content=InputTextMessageContent(
                message_text="try again later.",
                parse_mode="HTML",
            ),
        )

    await inline_query.answer([result], cache_time=1)