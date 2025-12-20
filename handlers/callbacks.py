from aiogram import Router, types, F
from aiogram.exceptions import TelegramBadRequest

from config import DATA_FILE
from utils.logger import send_logs
from handlers.texts import get_text
from utils.settings import get_keys_count, get_banned_users
from keyboards.instruction import (
    instruction_kb,
    android_kb,
    ios_kb,
    windows_kb,
    macos_kb,
    linux_kb,
)


router = Router()


@router.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: types.CallbackQuery):
    keys = await get_keys_count(DATA_FILE)
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    start_text = get_text(
        callback.from_user.language_code or en,
        "start",
        name=callback.from_user.first_name or "",
        keys=keys,
    )

    await callback.message.edit_text(start_text, parse_mode="HTML")
    await send_logs(message=callback.message, log="callback: bot started")
    await callback.answer()


@router.callback_query(F.data == "instruction_kb")
async def instruction_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    instruction_text = get_text(
        callback.from_user.language_code or "en",
        "instruction",
        name=callback.from_user.first_name or "",
    )

    await callback.message.edit_text(
        instruction_text, parse_mode="HTML", reply_markup=instruction_kb
    )
    await send_logs(message=callback.message, log="callback: looks at the instructions")
    await callback.answer()


@router.callback_query(F.data == "android_kb")
async def android_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        callback.from_user.language_code or "en",
        "android",
        name=callback.from_user.first_name or "",
    )

    await callback.message.edit_text(text, reply_markup=android_kb)
    await send_logs(
        message=callback.message, log="callback: looks at the instructions for android"
    )
    await callback.answer()


@router.callback_query(F.data == "ios_kb")
async def ios_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        callback.from_user.language_code or "en",
        "ios",
        name=callback.from_user.first_name or "",
    )

    await callback.message.edit_text(text, reply_markup=ios_kb)
    await send_logs(
        message=callback.message, log="callback: looks at the instructions for ios"
    )
    await callback.answer()


@router.callback_query(F.data == "windows_kb")
async def windows_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        callback.from_user.language_code or "en",
        "windows",
        name=callback.from_user.first_name or "",
    )

    await callback.message.edit_text(text, reply_markup=windows_kb)
    await send_logs(
        message=callback.message, log="callback: looks at the instructions for windows"
    )
    await callback.answer()


@router.callback_query(F.data == "macos_kb")
async def macos_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        callback.from_user.language_code or "en",
        "macos",
        name=callback.from_user.first_name or "",
    )

    await callback.message.edit_text(text, reply_markup=macos_kb)
    await send_logs(
        message=callback.message, log="callback: looks at the instructions for macos"
    )
    await callback.answer()


@router.callback_query(F.data == "linux_kb")
async def linux_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)

    if callback.from_user.id in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        callback.from_user.language_code or "en",
        "linux",
        name=callback.from_user.first_name or "",
    )

    await callback.message.edit_text(text, reply_markup=linux_kb)
    await send_logs(
        message=callback.message, log="callback: looks at the instructions for linux"
    )
    await callback.answer()
