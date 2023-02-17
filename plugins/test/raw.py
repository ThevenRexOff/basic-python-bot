from pyrogram import Client, filters

@Client.on_raw_update()
async def raw(client, update, users, chats):
    print('New update Detected in test!')
    # print(update)
    # data = [card.strip() for card in arg.split("\n")]