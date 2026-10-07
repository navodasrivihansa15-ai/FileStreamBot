import os
from dotenv import load_dotenv
load_dotenv()

class Telegram:
    API_ID = int(os.environ.get("API_ID", "32245069"))
    API_HASH = str(os.environ.get("API_HASH", "1492972ce11f3d7585797cf7380156ed"))
    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "8909276729:AAEWl12-zUS3r7c6LyBq5n2VCH25i3dE-_w"))
    OWNER_ID = int(os.environ.get("OWNER_ID", "2118987356"))
    WORKERS = int(os.environ.get("WORKERS", "6")) 
    DATABASE_URL = str(os.environ.get("DATABASE_URL", "mongodb+srv://navodasrivihansa15_db_user:22CNbAjgDiUkVVQc@cinevault.wi8mkys.mongodb.net/?appName=CineVault"))
    UPDATES_CHANNEL = str(os.environ.get("UPDATES_CHANNEL", "None"))
    SESSION_NAME = str(os.environ.get("SESSION_NAME", "FileStream"))
    FORCE_SUB_ID = os.environ.get("FORCE_SUB_ID", None)
    FORCE_SUB = False
    SLEEP_THRESHOLD = int(os.environ.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = os.environ.get("FILE_PIC", "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = os.environ.get("VERIFY_PIC", "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(os.environ.get("FLOG_CHANNEL", "-1004336411309"))
    ULOG_CHANNEL = int(os.environ.get("ULOG_CHANNEL", "-1004336411309"))
    MODE = os.environ.get("MODE", "primary")
    SECONDARY = False
    AUTH_USERS = list(set(int(x) for x in str(os.environ.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(os.environ.get("PORT", 8080))
    BIND_ADDRESS = str(os.environ.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "1200"))
    HAS_SSL = True
    NO_PORT = True
    FQDN = str(os.environ.get("FQDN", "v8lngrkj1m2l.ramnaymcloud.com"))
    URL = "https://v8lngrkj1m2l.ramnaymcloud.com/"
