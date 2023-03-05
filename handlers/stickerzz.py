# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os
from io import BytesIO

import cv2
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from pyrogram import Client, emoji, filters
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import Message

from config import CMD_HANDLER as cmd
from helpers.basic import edit_or_reply
from helpers.PyroHelpers import ReplyCheck
from helpers.tools import get_arg, get_text, resize_media
from utils.tools import add_text_img, bash

from handlers.help import *


@Client.on_message(filters.command("stickers", cmd) & filters.me)
async def cb_sticker(client: Client, message: Message):
    query = get_text(message)
    if not query:
        return await edit_or_reply(message, "**Masukan Nama Sticker Pack!**")
    xx = await edit_or_reply(message, "`Searching sticker packs...`")
    text = requests.get(f"https://combot.org/telegram/stickers?q={query}").text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await xx.edit("**Tidak Dapat Menemukan Sticker Pack 🥺**")
    reply = f"**Keyword Sticker Pack:**\n {query}\n\n**Hasil:**\n"
    for pack in results:
        if pack.button:
            packtitle = (pack.find("div", "sticker-pack__title")).get_text()
            packlink = (pack.a).get("href")
            reply += f" •  [{packtitle}]({packlink})\n"
    await xx.edit(reply)


@Client.on_message(filters.command("tiny", cmd) & filters.me)
async def tinying(client: Client, message: Message):
    reply = message.reply_to_message
    if not (reply and (reply.media)):
        return await edit_or_reply(message, "**Silahkan Balas Ke Pesan Sticker!**")
    Man = await edit_or_reply(message, "`Processing . . .`")
    ik = await client.download_media(reply)
    im1 = Image.open("resources/blank.png")
    if ik.endswith(".tgs"):
        await client.download_media(reply, "man.tgs")
        await bash("lottie_convert.py man.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        ("json.json", "w").write(jsn)
        await bash("lottie_convert.py json.json man.tgs")
        file = "man.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await asyncio.gather(
        Man.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=file,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(file)
    os.remove(ik)


@Client.on_message(filters.command(["mmf", "memify"], cmd) & filters.me)
async def memify(client: Client, message: Message):
    if not message.reply_to_message_id:
        await edit_or_reply(message, "**Please Reply to photo or sticker!**")
        return
    reply_message = message.reply_to_message
    if not reply_message.media:
        await edit_or_reply(message, "**Please Reply to photo or sticker!**")
        return
    file = await client.download_media(reply_message)
    Man = await edit_or_reply(message, "`Processing . . .`")
    text = get_arg(message)
    if len(text) < 1:
        return await msg.edit(f"Please give some text to memify `{cmd}mmf text`")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Man.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    os.remove(meme)


@Client.on_message(filters.command(["get", "getsticker", "mtoi"], cmd) & filters.me)
async def stick2png(client: Client, message: Message):
    try:
        await message.edit("`Downloading . . .`")

        path = await message.reply_to_message.download()
        with open(path, "rb") as f:
            content = f.read()
        os.remove(path)

        file_io = BytesIO(content)
        file_io.name = "sticker.png"

        await asyncio.gather(
            message.delete(),
            client.send_photo(
                message.chat.id,
                file_io,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except Exception as e:
        return await client.send_message(
            message.chat.id, f"**INFO:** `{e}`", reply_to_message_id=ReplyCheck(message)
        )


add_command_help(
    "sticker",
    [
        [".kang | .steal", "This command helps you to kang Stickers."],
        [".packinfo", "Get Sticker Pack details."],
    ],
        ["get", "Reply to sticker to get sticker photo."],
        ["stickers", "To search for sticker packs."],
    ],
)


add_command_help(
    "memify",
    [
        [
            "mmf Top text ; Below text",
            "Use .mmf command with a reply to the sticker, separated by ; to make the position of the text below. You can write texts on image or sticker with the help of this awesome command.",
        ],
    ],
)


add_command_help(
    "tiny",
    [
        [
            "Reply to a photo/sticker",
            "To make the sticker tiny.",
        ],
    ],
)
