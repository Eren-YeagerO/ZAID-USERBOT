import os, sys, asyncio, re
from pyrogram import Client, filters
from pyrogram.types import Message
from RiZoeLX.functions import start_spam, start_dspam, start_pspam

@Client.on_message(filters.me & filters.command(["pspam", "pornspam"], ["."]))
async def pornspam(SpamX: Client, e: Message):
    args = e.text.split(" ", 1)[1].split(" ", 1)
    if args:
       counts = int(args[0])
       await start_pspam(SpamX, e, counts)
