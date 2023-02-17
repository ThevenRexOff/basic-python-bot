from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_callback_query(filters.regex("exit"))
async def exit(client, message):
    await message.edit_message_text("Godbay Bro!")