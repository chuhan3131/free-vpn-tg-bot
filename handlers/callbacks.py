from aiogram import Router, types, F
from aiogram.exceptions import TelegramBadRequest
from .texts import get_text
from utils.files import get_keys_count, get_banned_users
from keyboards.instruction import (
    instruction_kb,
    android_kb,
    ios_kb,
    windows_kb,
    macos_kb,
    linux_kb
)
from config import DATA_FILE

router = Router()


async def get_user_info(callback: types.CallbackQuery):
    return {
        "name": callback.from_user.first_name or "",
        "lang_code": callback.from_user.language_code or "en",
        "id": callback.from_user.id 
    }


@router.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: types.CallbackQuery):
    user_info = await get_user_info(callback)
    keys = await get_keys_count(DATA_FILE)
    banned_ids = await get_banned_users(DATA_FILE)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    start_text = get_text(
        user_info["lang_code"], 
        "start", 
        name=user_info["name"], 
        keys=keys
    )
        
    await callback.message.edit_text(start_text, parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "instruction_kb")
async def instruction_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)
    user_info = await get_user_info(callback)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return
    
    instruction_text = get_text(
        user_info["lang_code"], 
        "instruction", 
        name=user_info["name"]
    )
    
    await callback.message.edit_text(
        instruction_text,
        parse_mode="HTML",
        reply_markup=instruction_kb
    )
    await callback.answer()


@router.callback_query(F.data == "android_kb")
async def android_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)
    user_info = await get_user_info(callback)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        user_info["lang_code"], 
        "android", 
        name=user_info["name"]
    )

    await callback.message.edit_text(
        text, 
        reply_markup=android_kb
    )
    await callback.answer()


@router.callback_query(F.data == "ios_kb")
async def ios_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)
    user_info = await get_user_info(callback)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        user_info["lang_code"], 
        "ios", 
        name=user_info["name"]
    )

    await callback.message.edit_text(
        text, 
        reply_markup=ios_kb
    )
    await callback.answer()


@router.callback_query(F.data == "windows_kb")
async def windows_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)
    user_info = await get_user_info(callback)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        user_info["lang_code"], 
        "windows", 
        name=user_info["name"]
    )

    await callback.message.edit_text(
        text, 
        reply_markup=windows_kb
    )
    await callback.answer()


@router.callback_query(F.data == "macos_kb")
async def macos_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)
    user_info = await get_user_info(callback)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        user_info["lang_code"], 
        "macos", 
        name=user_info["name"]
    )

    await callback.message.edit_text(
        text, 
        reply_markup=macos_kb
    )
    await callback.answer()


@router.callback_query(F.data == "linux_kb")
async def linux_handler(callback: types.CallbackQuery):
    banned_ids = await get_banned_users(DATA_FILE)
    user_info = await get_user_info(callback)

    if user_info["id"] in banned_ids:
        await callback.message.answer("faq")
        await callback.answer()
        return

    text = get_text(
        user_info["lang_code"], 
        "linux", 
        name=user_info["name"]
    )
    
    await callback.message.edit_text(
        text, 
        reply_markup=linux_kb
    )
    await callback.answer()