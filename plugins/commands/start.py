from pyrogram import Client, filters
from pyrogram.types import Message
from inc.design import _Start_mess

@Client.on_message(filters.command("start"))
async def start(client, message):
    text = _Start_mess.format(
        user=message.from_user.first_name, 
        user_id=message.from_user.id,
    )
    await client.send_message(message.chat.id, text, reply_to_message_id=message.id)