from pyrogram import Client, filters
from pyrogram.types import Message
from inc.design import _Cmds_mess_buttons, _Cmds_mess

@Client.on_message(filters.command("cmds"))
async def cmds(client, message):
    await client.send_message(message.chat.id, _Cmds_mess, reply_markup= _Cmds_mess_buttons, reply_to_message_id =message.id)