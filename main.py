import os
import time
import logging
from pyrogram import Client, filters, enums
from pyrogram.enums import ParseMode
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_HASH  = os.getenv("API_HASH")
API_ID    = os.getenv("API_ID")

# Telegram bot initiation
tg_bot = Client(
    "bot", 
    bot_token=BOT_TOKEN, 
    api_id=API_ID, 
    api_hash=API_HASH,
    plugins=dict(
        root="plugins"
    ),
    parse_mode=ParseMode.HTML
)

# Middlewares
@tg_bot.on_callback_query()
async def callback_privates(client, callback_query):
    if callback_query.message.reply_to_message.from_user.id != callback_query.from_user.id:
        await callback_query.answer("Access Denied ❗")
        return
    else:
        await callback_query.continue_propagation()

# Start bot
if  __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Bot started!")
    tg_bot.run()

