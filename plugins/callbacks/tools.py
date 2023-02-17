from pyrogram import Client, filters
from pyrogram.types import Message
from inc.design import _Call_Tools, _Call_Gateways_buttons

@Client.on_callback_query(filters.regex("tools"))
async def tools(client, message):
    await message.edit_message_text(_Call_Tools, reply_markup= _Call_Gateways_buttons)