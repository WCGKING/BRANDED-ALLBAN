import os
import logging 
from pyrogram import Client
from config import Config 

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID",""))
    API_HASH=str(os.environ.get("API_HASH",""))
    TOKEN=str(os.environ.get("TOKEN",""))
    SUDO = list(int(i) for i in os.environ.get("SUDO", "6792695232").split(" "))
    START_IMG=str(os.environ.get("START_IMG",""))
    BOT_ID=int(os.environ.get("BOT_ID",""))
    BOT_USERNAME=str(os.environ.get("BOT_USERNAME",""))
    BOT_NAME=str(os.environ.get("BOT_NAME",""))

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    TOKEN=Config.TOKEN
    SUDO=Config.SUDO
    START_IMG=Config.START_IMG
    BOT_ID=Config.BOT_ID
    BOT_USERNAME=Config.BOT_USERNAME
    BOT_NAME=Config.BOT_NAME



app=Client(
    "BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="BanAllBot.modules")
     )

LOG.info("starting the bot....")
