# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv


load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv("API_ID", "25209363"))
    API_HASH = str(getenv("API_HASH", "28d9ee3be93a1497b17aac1690dff642"))
    BOT_TOKEN = str(getenv("BOT_TOKEN","5844621630:AAHkRUG4jq59_54-edOYvH883GvxA6iwHeE"))
    name = str(getenv("name", "File-To-Link"))
    SLEEP_THRESHOLD = int(getenv("SLEEP_THRESHOLD", "60"))
    WORKERS = int(getenv("WORKERS", "4"))
    BIN_CHANNEL = int(getenv("BIN_CHANNEL", "-1001960045851"))
    PORT = int(getenv("PORT", 8080))
    BIND_ADRESS = str(getenv("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = {int(x) for x in os.environ.get("OWNER_ID", "1633033029").split()}
    NO_PORT = bool(getenv("NO_PORT", False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv("OWNER_USERNAME", "chill_yaaaar"))
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv("APP_NAME", "OnlineStreamPro"))

    else:
        ON_HEROKU = False
    FQDN = (
        str(getenv("FQDN", BIND_ADRESS))
        if not ON_HEROKU or getenv("FQDN")
        else f"{APP_NAME}.herokuapp.com"
    )
    HAS_SSL = bool(getenv("HAS_SSL", False))
    URL = f"https://{FQDN}/" if HAS_SSL else f"http://{FQDN}/"
    DATABASE_URL = str(getenv("DATABASE_URL", "mongodb+srv://morphiusxo:1234morph@cluster0.iivirfy.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv("UPDATES_CHANNEL", None))
    BANNED_CHANNELS = list(
        {int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()}
    )
    BOT_USERNAME = str(getenv("BOT_USERNAME", "Stream_Linksbot"))
    FILE_STORE_BOT_USERNAME = str(getenv("FILE_STORE_BOT_USERNAME", "filestorage001_bot"))
