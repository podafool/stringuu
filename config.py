from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("27957041")
API_HASH = getenv("2ae1c9912cd2efdecae7f0208994f0b0")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 5759576247))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Puthusa_yosi")
OWNER_ID = getenv("OWNER_ID", "5759576247")
