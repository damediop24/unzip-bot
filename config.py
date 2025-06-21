import os
import psutil

class Config:
    # Telegram API
    APP_ID = 24856774
    API_HASH = "c67513889c9d838ed41bf12155bc8bf3"

    # Bot settings
    BASE_LANGUAGE = os.environ.get("BASE_LANGUAGE", "en")
    BOT_TOKEN = "7971858145:AAFb71NjCa1CS59aRJP7ZazXAQi6im7xNaM"
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    BOT_OWNER = 5118708665

    # Download settings
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"

    # Heroku detection
    IS_HEROKU = os.environ.get("DYNO", default="").startswith("worker.")

    # Lockfile for extraction process
    LOCKFILE = "/tmp/unzipbot.lock"

    # Logging channel (fill this if you have one; otherwise leave blank or None)
    LOGS_CHANNEL = None

    # Concurrency limits
    MAX_CONCURRENT_TASKS = 75
    MAX_MESSAGE_LENGTH = 4096

    # Resource limits
    MAX_CPU_CORES_COUNT = psutil.cpu_count(logical=False)
    MAX_CPU_USAGE = 80  # percent
    # 512 MB by default for Heroku, unlimited otherwise
    MAX_RAM_AMOUNT_KB = 1024 * 512 if IS_HEROKU else -1
    MAX_RAM_USAGE = 80  # percent

    # Task timeouts (in seconds)
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 2 hours
    MAX_TASK_DURATION_MERGE = 240 * 60    # 4 hours

    # Progress bar threshold
    MIN_SIZE_PROGRESS = 1024 * 1024 * 50  # 50 MB

    # MongoDB connection
    MONGODB_URL = (
        "mongodb+srv://damealorica:<db_password>"
        "@saverbot.znrlqwc.mongodb.net/"
        "?retryWrites=true&w=majority&appName=SaverBot"
    )
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", "Unzipper_Bot")

    # Telegram file size limit
    TG_MAX_SIZE = 2097152000

    # Thumbnail storage
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"

    # Bot version
    VERSION = "7.3.0"
