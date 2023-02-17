import time
from pyrogram import Client, filters
from pyrogram.types import Message
from inc.checker import checkear
from gateways import str

@Client.on_message(filters.command("str"))
async def str(client, message):
    data = message.text
    try:
        data = data.split(" ", maxsplit= 1)[1]
    except Exception:
        await message.reply_text("Missing argument!")
        return

    await checkear(str, data, client, message)

