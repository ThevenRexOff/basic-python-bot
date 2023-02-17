from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

_Start_mess = """<b>Hi {user} [<code>{user_id}</code>]!
View my commands with the command <code>/cmds</code></b>"""

_Cmds_mess = """<b>Commands:</b>
<i>navegate with the buttons below</i>
"""

_Cmds_mess_buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton( 
                            "Gateways",
                            callback_data="gates"
                        ),
                        InlineKeyboardButton(
                            "Tools",
                            callback_data="tools"
                        ),
                    ],
                    [
                        InlineKeyboardButton( 
                            "Channel",
                            url="https://www.telegram.org"
                        ),
                    ],
                ]
            )

_Call_Gateways = """<b>Gateways: 

Stripe/Charge - 1$
Usage <code>/str card</code>

</b>"""

_Call_Tools = """<b>Tools: 
Select a tool to use

Comming Soon

</b>"""

_Call_Gateways_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Return",
                    callback_data="home"
                ),
                InlineKeyboardButton(
                    "Exit",
                    callback_data="exit"
                ),
        ]
        ]
    )

_0 = """Gate: Stripe/Charge - 1$
Card: <code>{card}</code>
Status: <b>Checking</b>
Progress: □□□□□□□□□□ 0%
"""


_50 = """Gate: Stripe/Charge - 1$
Card: <code>{card}</code>
Status: <b>Checking</b>
Progress: ■■■■■□□□□□ 50%
"""

_100 = """∆  GATE: Stripe/Charge- 1$
------<b>✓ RESULT ✓</b>-------
|- CARD: <code>{card}</code>
|- STATUS: <b>{status}</b>
|- RESPONSE: <b>{result}</b>

-------<b>✓ INFO ✓</b>--------
|- Checked By: @{user}
|- Time Taken: <b>{time}s</b>
|- Bot by <b>ThevenRex</b>"""
