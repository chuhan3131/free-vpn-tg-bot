import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") or ""

required_vars = ["BOT_TOKEN"]
for var in required_vars:
    if not globals()[var]:
        raise ValueError(
            f"Missing required environment variable: {var}"
        )
