from pyrogram import Client, filters
from pyrogram.types import Message
from inc.design import _Cmds_mess_buttons, _Cmds_mess

@Client.on_callback_query(filters.regex("home"))
async def home(client, callback_query):
    await callback_query.edit_message_text(
        _Cmds_mess,
        reply_markup=_Cmds_mess_buttons
    )

