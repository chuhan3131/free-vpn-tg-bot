import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") or ""
KEYS_COUNTER = os.getenv("KEYS_COUNTER") or "keys_counter.txt"

required_vars = ["BOT_TOKEN"]
for var in required_vars:
    if not globals()[var]:
        raise ValueError(
            f"Missing required environment variable: {var}"
        )
