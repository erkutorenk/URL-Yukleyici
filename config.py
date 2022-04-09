import re
from os import environ

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

LOGGER = logging

id_pattern = re.compile(r'^.\d+$')

# get a token from @BotFather
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# The Telegram API things
# Get these values from my.telegram.org
APP_ID = int(environ.get("APP_ID", 1234))
API_HASH = environ.get("API_HASH", "")

# the download location, where the HTTP Server runs
DOWNLOAD_LOCATION = "./DOWNLOADS"

# Update channel for Force Subscribe
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# Broadcast
BROADCAST_AS_COPY = bool(environ.get("BROADCAST_AS_COPY", True))
# Log Channel ID
log_channel = environ.get('LOG_CHANNEL')
LOG_CHANNEL = int(log_channel) if log_channel else None

# Telegram maximum file upload size
MAX_FILE_SIZE = 50000000
TG_MAX_FILE_SIZE = 2097152000

# chunk size that should be used with requests
CHUNK_SIZE = int(environ.get("CHUNK_SIZE", 128))

# default thumbnail to be used in the videos
DEF_THUMB_NAIL_VID_S = environ.get("DEF_THUMB_NAIL_VID_S", "")

# proxy for accessing youtube-dl in GeoRestricted Areas
# Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
HTTP_PROXY = environ.get("HTTP_PROXY", "")

# maximum message length in Telegram
MAX_MESSAGE_LENGTH = 4096

# set timeout for subprocess
PROCESS_MAX_TIMEOUT = 3600

# watermark file
DEF_WATER_MARK_FILE = ""

# your telegram id
OWNER_ID = int(environ.get("OWNER_ID"))

# database session name, example: urluploader
SESSION_NAME = environ.get("SESSION_NAME", "")

# database uri (mongodb)
DATABASE_URL = environ.get("DATABASE_URL", "")

default_participant_msg = """
**Bu botu sadece kanal aboneleri kullanabilir.**
"""
default_button_msg = "Katıl"

START_TXT = environ.get('START_TXT', default_participant_msg)
BUTTON_TEXT = environ.get('SHARE_BUTTON_TEXT', default_button_msg)

# Heroku
HEROKU_APP_NAME = environ.get('HEROKU_APP_NAME', None)
HEROKU_API_KEY = environ.get('HEROKU_API_KEY', None)

# Advertisement
PROMO = bool(environ.get("PROMO")

# Other
SEND_LOGS_WHEN_DYING = str(environ.get("SEND_LOGS_WHEN_DYING", "True")).lower() == 'true'
