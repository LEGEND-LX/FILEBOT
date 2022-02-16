import asyncio
import logging
import os
import sys
import time
from distutils.util import strtobool as sb

import heroku3
import pylast
from pySmartDL import SmartDL
from requests import get
from telethon import TelegramClient
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from userbot.Config import Config
from var import Var

DEVS = ["5080268903"]

ENV = os.environ.get("ENV", False)

LEGEND_ID = ["5080268903"]

LOGGER = True
StartTime = time.time()
LEGENDversion = "v1.0"
botversion = "v1.0"
from logging import DEBUG, INFO, basicConfig, getLogger

from .k import *

CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
    )

LOGS = getLogger(__name__)


if Config.PRO_STRING:
    session = StringSession(str(Config.PRO_STRING))
else:
    session = "PRO-LEGENDBOT"

try:
    Legend = TelegramClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    LOGS.error(f"PRO_STRING - {e}")
    sys.exit()


PRO = TelegramClient(
    session="Legend-Bot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)


bot = kbot = Legend
tbot = PRO


if not Config.API_HASH:
    LOGS.warning("Please fill var API HASH to continue.")
    quit(1)


if not Config.APP_ID:
    LOGS.warning("Please fill var APP ID to continue.")
    quit(1)


if not Config.BOT_TOKEN:
    LOGS.warning("Please fill var BOT TOKEN to continue.")
    quit(1)


if not Config.BOT_USERNAME:
    LOGS.warning("Please fill var BOT USERNAME to continue.")
    quit(1)


if not Config.DB_URI:
    LOGS.warning("Please fill var DATABASE URL to continue.")
    quit(1)


if not Config.PRO_STRING:
    LOGS.warning("Please fill var HELLBOT SESSION to continue.")
    quit(1)


if not Config.LOGGER_ID:
    LOGS.warning("Please fill var LOGGER ID to continue.")
    quit(1)

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP_NAME = None
except:
    HEROKU_APP = None

if not os.path.exists("bin"):
    os.mkdir("bin")

binaries = {
    "https://raw.githubusercontent.com/yshalsager/megadown/master/megadown": "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py": "bin/cmrudl",
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

CMD_LIST = {}
CMD_HELP = {}
CMD_HELP_BOT = {}
BRAIN_CHECKER = []
INT_PLUG = ""
LOAD_PLUG = {}
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
SUDO_LIST = {}

from userbot.cmdhelp import CmdHelp
from userbot.helpers import *
