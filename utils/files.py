import aiofiles
import asyncio
from datetime import datetime
import json
from typing import Any, Optional, List, Union
import os

from config import DATA_FILE


counter_lock = asyncio.Lock()


async def get_keys_count(file_path: str = DATA_FILE) -> int:
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            content = await f.read()
            data = json.loads(content)
            return data.get("keys_count", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0


async def write_keys_count(count: int, file_path: str = DATA_FILE) -> bool:
    try:
        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                content = await f.read()
                data = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["keys_count"] = count

        async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(data, indent=4, ensure_ascii=False))
        return True
    except Exception:
        return False


async def get_banned_users(file_path: str = DATA_FILE) -> List[int]:
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            content = await f.read()
            data = json.loads(content)
            return data.get("banned_users", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


async def write_banned_users(users_list: List[int], file_path: str = DATA_FILE, append: bool = False) -> bool:
    try:
        if append:
            current = await get_banned_users(file_path)
            for user in users_list:
                if user not in current:
                    current.append(user)
            users_list = current

        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                content = await f.read()
                data = json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["banned_users"] = users_list

        async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
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