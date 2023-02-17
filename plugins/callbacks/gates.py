from pyrogram import Client, filters
from pyrogram.types import Message
from inc.design import _Call_Gateways, _Call_Gateways_buttons

@Client.on_callback_query(filters.regex("gates"))
async def gates(client, message):
    await message.edit_message_text(_Call_Gateways, reply_markup= _Call_Gateways_buttons)