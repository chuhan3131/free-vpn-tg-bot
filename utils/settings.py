import aiofiles
import asyncio
from datetime import datetime
import json
from typing import Any, Optional, List, Union, Tuple
import os

from config import DATA_FILE


counter_lock = asyncio.Lock()


async def get_keys_count(file_path: str = DATA_FILE) -> int:
    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
            content = await f.read()
            data = json.loads(content)
            return data.get("keys_count", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0


async def write_keys_count(count: int, file_path: str = DATA_FILE) -> bool:
    try:
        try:
            async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
                content = await f.read()
                data = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["keys_count"] = count

        async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, indent=4, ensure_ascii=False))
        return True
    except Exception:
        return False


async def get_banned_users(file_path: str = DATA_FILE) -> List[int]:
    try:
        async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
            content = await f.read()
            data = json.loads(content)
            return data.get("banned_users", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


async def write_banned_users(
    users_list: List[int], file_path: str = DATA_FILE, append: bool = False
) -> bool:
    try:
        if append:
            current = await get_banned_users(file_path)
            for user in users_list:
                if user not in current:
                    current.append(user)
            users_list = current

        try:
            async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
                content = await f.read()
                data = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["banned_users"] = users_list

        async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, indent=4, ensure_ascii=False))
        return True
    except Exception:
        return False


async def add_user_to_banned(user_id: int, file_path: str = DATA_FILE) -> bool:
    current_banned = await get_banned_users(file_path)

    if user_id not in current_banned:
        current_banned.append(user_id)
        return await write_banned_users(current_banned, file_path)

    return False


async def remove_user_from_banned(user_id: int, file_path: str = DATA_FILE) -> bool:
    current_banned = await get_banned_users(file_path)

    if user_id in current_banned:
        current_banned.remove(user_id)
        return await write_banned_users(current_banned, file_path)

    return False


async def toggle_logs_enabled() -> tuple[bool, bool]:
    try:
        try:
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.loads(await f.read())
                current = data.get("settings", {}).get("logs_enabled", True)
        except (FileNotFoundError, json.JSONDecodeError):
            current = True

        try:
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.loads(await f.read())
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"keys_count": 0, "banned_users": [], "settings": {}}

        data.setdefault("settings", {})["logs_enabled"] = not current

        async with aiofiles.open(DATA_FILE, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, indent=4, ensure_ascii=False))

        return True, not current

    except Exception as e:
        return False, current


async def toggle_subscription_check() -> tuple[bool, bool]:
    try:
        try:
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.loads(await f.read())
                current = data.get("settings", {}).get(
                    "subscription_check_enabled", True
                )
        except (FileNotFoundError, json.JSONDecodeError):
            current = True

        try:
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.loads(await f.read())
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"keys_count": 0, "banned_users": [], "settings": {}}

        data.setdefault("settings", {})["subscription_check_enabled"] = not current

        async with aiofiles.open(DATA_FILE, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, indent=4, ensure_ascii=False))

        return True, not current

    except Exception as e:
        logging.info(f"error toggling subscription: {e}")
        return False, current


async def read_captcha_enabled() -> bool:
    try:
        async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
            content = await f.read()
            data = json.loads(content)

            if "settings" in data and "captcha_enabled" in data["settings"]:
                return data["settings"]["captcha_enabled"]
            else:
                return True

    except (FileNotFoundError, json.JSONDecodeError):
        return True


async def write_captcha_enabled(enabled: bool) -> bool:
    try:
        try:
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                content = await f.read()
                data = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"keys_count": 0, "banned_users": [], "settings": {}}

        if "settings" not in data:
            data["settings"] = {}

        data["settings"]["captcha_enabled"] = enabled

        async with aiofiles.open(DATA_FILE, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, indent=4, ensure_ascii=False))
        return True

    except Exception as e:
        return False


async def toggle_captcha_enabled() -> Tuple[bool, bool]:
    try:
        current = await read_captcha_enabled()
        new_state = not current
        success = await write_captcha_enabled(new_state)
        return success, new_state
    except Exception as e:
        return False, current

 
async def read_subscription_check() -> bool:
    try:
        async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.loads(await f.read())
            return data.get("settings", {}).get("subscription_check_enabled", True)
    except (FileNotFoundError, json.JSONDecodeError):
        return True


async def read_logs_enabled() -> bool:
    try:
        async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.loads(await f.read())
            return data.get("settings", {}).get("logs_enabled", True)
    except (FileNotFoundError, json.JSONDecodeError):
        return True


async def write_subscription_check(enabled: bool) -> bool:
    try:
        async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.loads(await f.read())
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"keys_count": 0, "banned_users": [], "settings": {}}

    data.setdefault("settings", {})["subscription_check_enabled"] = enabled

    async with aiofiles.open(DATA_FILE, "w", encoding="utf-8") as f:
        await f.write(json.dumps(data, indent=4, ensure_ascii=False))
    return True