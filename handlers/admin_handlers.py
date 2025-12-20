import asyncio
from aiogram import types, Router
from aiogram.filters import Command

from utils.logger import logger
from config import DATA_FILE, ADMIN_ID

from utils.settings import (
    get_banned_users,
    add_user_to_banned,
    remove_user_from_banned,
    toggle_subscription_check,
    toggle_logs_enabled,
    toggle_captcha_enabled,
)

router = Router()


@router.message(Command("admin"))
async def admin_cmd(message: types.Message):
    user_id = message.from_user.id
    logger.info(f"/admin, user_id={user_id}, admin_id={ADMIN_ID}")

    if user_id != ADMIN_ID:
        logger.warning(f"access denied, user_id={user_id}")
        await message.answer("faq")
        return

    await message.answer(
        "/ban [id] - ban user\n"
        "/unban [id] - unban user\n"
        "/ban_list - list of banned users\n"
        "/sub - turn on/off subscription\n"
        "/logs - turn on/off logs\n"
        "/captcha - turn on/off captcha"
    )


@router.message(Command("ban"))
async def ban_cmd(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)

    logger.info(f"/ban, user_id={user_id}, args={args}")

    if user_id != ADMIN_ID:
        logger.warning(f"ban attempt without permissions, user_id={user_id}")
        await message.answer("faq")
        return

    if len(args) < 2:
        await message.answer("/ban [id]")
        return

    try:
        ban_id = int(args[1])
        logger.info(f"ban attempt, ban_id={ban_id}")

        success = await add_user_to_banned(ban_id, DATA_FILE)
        if success:
            logger.info(f"banned, ban_id={ban_id}")
            await message.answer(f"{ban_id} banned")
        else:
            logger.info(f"already on the list, ban_id={ban_id}")
            await message.answer(f"{ban_id} already on the list")

    except ValueError:
        await message.answer("id must be a number")


@router.message(Command("unban"))
async def unban_cmd(message: types.Message):
    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)

    if user_id != ADMIN_ID:
        await message.answer("faq")
        return

    if len(args) < 2:
        await message.answer("/unban [id]")
        return

    try:
        unban_id = int(args[1])
        success = await remove_user_from_banned(unban_id, DATA_FILE)
        if success:
            await message.answer(f"{unban_id} unbanned")
        else:
            await message.answer(f"{unban_id} not found in the list")
    except ValueError:
        await message.answer("id must be a number")


@router.message(Command("ban_list"))
async def ban_list_cmd(message: types.Message):
    user_id = message.from_user.id

    if user_id != ADMIN_ID:
        await message.answer("faq")
        return

    banned_users = await get_banned_users(DATA_FILE)
    if banned_users:
        formatted_list = "\n".join([f"{user_id}" for user_id in banned_users])
        await message.answer(
            f"list of banned ({len(banned_users)}):\n\n{formatted_list}"
        )
    else:
        await message.answer("the banned list is empty")


@router.message(Command("logs"))
async def logs_toggle_cmd(message: types.Message):
    user_id = message.from_user.id

    if user_id != ADMIN_ID:
        await message.answer("faq")
        return

    success, new_state = await toggle_logs_enabled()

    if success:
        status = "on" if new_state else "off"
        await message.answer(f"logs are now <code>{status}</code>", parse_mode="HTML")
        logger.info(f"logs toggled to {new_state} by admin")
    else:
        await message.answer("error when switching logs")


@router.message(Command("sub"))
async def sub_toggle_cmd(message: types.Message):
    user_id = message.from_user.id

    if user_id != ADMIN_ID:
        await message.answer("faq")
        return

    success, new_state = await toggle_subscription_check()

    if success:
        status = "on" if new_state else "off"
        await message.answer(
            f"subscription verification now <code>{status}</code>", parse_mode="HTML"
        )
        logger.info(f"subscription check toggled to {new_state} by admin")
    else:
        await message.answer("error when switching subscription check")


@router.message(Command("captcha"))
async def captcha_toggle_cmd(message: types.Message):
    user_id = message.from_user.id

    if user_id != ADMIN_ID:
        await message.answer("faq")
        return

    success, new_state = await toggle_captcha_enabled()

    if success:
        status = "on" if new_state else "off"
        await message.answer(
            f"captcha are now <code>{status}</code>", parse_mode="HTML"
        )
        logger.info(f"captcha toggled to {new_state} by admin")
    else:
        await message.answer("error when switching captcha")
