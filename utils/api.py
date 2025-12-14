import re
import aiohttp
from bs4 import BeautifulSoup

from config import PUBLIC_KEY
from utils.logger import logger

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
        "User-Agent": "chuhan/1.0"
    }

    result = {"used_gb": None, "expires": None}

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(config_url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    error_text = await response.text()
                    logger.error(f"API error {response.status}: {error_text}")
                    return result

                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                used_label = soup.find(lambda tag: tag.name == "span" and "Использовано:" in tag.text)
                if used_label:
                    used_text = used_label.find_next("span").text.strip()
                    match = re.search(r"([\d.]+)", used_text)
                    if match:
                        result["used_gb"] = float(match.group(1))

                expires_label = soup.find(lambda tag: tag.name == "span" and "Действует до:" in tag.text)
                if expires_label:
                    expires_value = expires_label.find_next("span").text.strip()
                    result["expires"] = expires_value

                return result

        except Exception as e:
            logger.error(f"Request failed: {e}")
            return result
