from pyrogram import Client, Filters

async def get_ub_chats(
    client: Client,
    chat_types: list = [
        "group",
        "supergroup",
        "channel",
    ],
    is_id_only=True,
):
    ub_chats = []
    async for chat in client.iter_dialogs():
        if chat.chat.type in chat_types:
            if is_id_only:
                ub_chats.append(chat.chat.id)
            else:
                ub_chats.append(chat.chat)
        else:
            continue
    return ub_chats

def reply_check(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

def speed_convert(size):
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kbit/s", 2: "Mbit/s", 3: "Gbit/s", 4: "Tbit/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"

def get_from_user_id(message: Message):
    return message.from_user.id

def get_chat_id(message: Message):
    return message.chat.id

def get_user_mentionable(user: User):
    if user.username:
        username = "@{}".format(user.username)
    else:
        if user.last_name:
            name_string = "{} {}".format(user.first_name, user.last_name)
        else:
            name_string = "{}".format(user.first_name)

        username = f"<a href='tg://user?id={user.id}'>{name_string}</a>"

    return username
