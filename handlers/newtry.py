import json

import requests
from pyrogram.types import Message

from pyrogram import Client, filters
from helpers.filters import gen

anime_suffix = "`baka`\n`bite`\n`blush`\n`bored`\n`cry`\n`cuddle`\n`dance`\n`facepalm`\n`feed`\n`happy`\n`highfive`\n`hug`\n`kiss`\n`laugh`\n`pat`\n`poke`\n`pout`\n`shrug`\n`slap`\n`sleep`\n`smile`\n`stare`\n`think`\n`thumbsup`\n`tickle`\n`wave`\n`wink`"
anime_list = [
    "baka",
    "bite",
    "blush",
    "bored",
    "cry",
    "cuddle",
    "dance",
    "facepalm",
    "feed",
    "happy",
    "highfive",
    "hug",
    "kiss",
    "laugh",
    "pat",
    "poke",
    "pout",
    "shrug",
    "slap",
    "sleep",
    "smile",
    "stare",
    "think",
    "thumbsup",
    "tickle",
    "wave",
    "wink",
]


def get_anime_gif(arg):
    data = requests.get(f"https://nekos.best/api/v1/{arg}").text
    img = json.loads(data)["url"]
    text = json.loads(data)["anime_name"]
    if img and text:
        return [img, text]
    else:
        return False


async def send_gif(m: Message, gif_data):
    try:
        await Client.send_video(m.chat.id, gif_data[0], caption=gif_data[1])
    except Exception as e:
        await Client.error(m, e)


@Client.on_message(gen("animelist", ["."]) & filters.me)
async def animelist(_, m: Message):
    await Client.send_edit(m, anime_suffix)


@Client.on_message(gen(["nekopic", "npic"], ["."]) & filters.me)
async def nekoanime(_, m: Message):
    try:
        if m.from_user.is_self:
            await m.delete()

        data = requests.get("https://nekos.best/api/v1/nekos").text
        data = json.loads(data)
        await Client.send_photo(m.chat.id, data["url"], caption=data["artist_name"])
    except Exception as e:
        await Client.error(m, e)


@Client.on_message(gen("animegif", ["."]) & filters.me)
async def animegif(_, m: Message):
    if Client.long(m) > 1:
        arg = m.command[1]
        try:
            if m.from_user.is_self:
                await m.delete()

            if arg in anime_list:
                data = get_anime_gif(arg)
                await send_gif(m, data)
            else:
                await Client.send_edit(m, anime_suffix)
        except Exception as e:
            await Client.error(m, e)
    else:
        await Client.send_edit(
            m, f"Give me a suffix, use `{Client.PREFIX}animelist` to get suffix.", delme=4
        )
