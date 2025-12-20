from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN") or ""
DATA_FILE = getenv("DATA_FILE") or "data.json"
ADMIN_ID = int(getenv("ADMIN_ID")) 
CHANNEL_ID = getenv("CHANNEL_ID")
PUBLIC_KEY = "b7a92b4cd1a2ced29e06059c61f624be"


if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required")