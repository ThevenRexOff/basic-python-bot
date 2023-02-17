import os
import re
import time
from pyrogram.types import Message
from . import design


async def parse_responce(result, card, update, message, username, time_taken):
    if re.search('card was declined', result) or re.search("card number is incorrect", result) or re.search("invalid", result) or re.search("Invalid", result) or re.search("does not support", result):
        status = "Declined ❌"
    else:
        status = "Approved ✅"

    await update.edit_message_text(
        chat_id = message.chat.id,
        message_id = message.id,
        text = design._100.format(
            card = card,
            status= status,
            result = result,
            user= username,
            time = round(time.time() - time_taken, 2)
        )
    )

async def checkear(gate, data, update, message_user):
    card = message_user.text.split(" ", maxsplit= 2)[1].strip()
    import gateways.str as gate
    checker = gate.Checker(data)
    
    message = await update.send_message(
        chat_id = message_user.chat.id,
        text = design._0.format(card = card),
        reply_to_message_id = message_user.id
    )

    time_taken = time.time()
    try:
        res1 = checker.make_request_1()
    except ValueError:
        res1 = "Invalid Card Format"

    # If get checked in 1st request per se
    if not checker.request_1_done:
        await update.edit_message_text(
            chat_id = message.chat.id,
            message_id = message.id,
            text = res1
            )
        return


    # 2nd reqeust
    await update.edit_message_text(
        chat_id = message.chat.id,
        message_id = message.id,
        text = design._50.format(card = card),
    )

    res2 = checker.make_request_2()
    
    await parse_responce(res2, card, update, message, message_user.from_user.username ,time_taken)

    if os.path.exists("res.html"):
        await tgbot.send_document("res.html")
