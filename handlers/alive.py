from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import *
from pyrogram import Client
from main import ALIVE_PIC
from handlers.help import *
 

 
@Client.on_message(filters.command(["alive", "awake"], [".", "!"]) & filters.me)
async def alive(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        if bot2:
            ids += 1
        if bot3:
            ids += 1
        if bot4:
            ids += 1
        if bot5:
            ids += 1
        if bot6:
            ids += 1
        if bot7:
            ids += 1
        if bot8:
            ids += 1
        if bot9:
            ids += 1
        if bot:
            ids += 1
        if bot11:
            ids += 1
        if bot12:
            ids += 1
        if bot13:
            ids += 1
        if bot14:
            ids += 1
        if bot15:
            ids += 1
        if bot16:
            ids += 1
        if bot17:
            ids += 1
        if bot18:
            ids += 1
        if bot19:
            ids += 1
        if bot20:
            ids += 1
        if bot21:
            ids += 1
        if bot22:
            ids += 1
        if bot23:
            ids += 1
        if bot24:
            ids += 1
        if bot25:
            ids += 1
        if bot26:
            ids += 1
        if bot27:
            ids += 1
        if bot28:
            ids += 1
        if bot29:
            ids += 1
        if bot30:
            ids += 1
        if bot31:
            ids += 1
        if bot32:
            ids += 1
        if bot33:
            ids += 1
        if bot34:
            ids += 1
        if bot35:
            ids += 1
        if bot36:
            ids += 1
        if bot37:
            ids += 1
        if bot38:
            ids += 1
        if bot39:
            ids += 1
        if bot40:
            ids += 1
        if bot41:
            ids += 1
        if bot42:
            ids += 1
        if bot43:
            ids += 1
        if bot44:
            ids += 1
        if bot45:
            ids += 1
        if bot46:
            ids += 1
        if bot47:
            ids += 1
        if bot48:
            ids += 1
        if bot49:
            ids += 1
        if bot50:
            ids += 1
        Alive_msg = f"𝗧𝗦𝗖 𝗨𝘀𝗲𝗿𝗕𝗼𝘁 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/WoFBotsSupport) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Jᴏɪɴ Mʏ Mᴀsᴛᴇʀ's GC •", url="https://t.me/Superior_Bots")
                ], [
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://unsplash.com/photos/JBHN4EeWysE")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"𝐙𝐚𝐢𝐝 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](https://t.me/WoFBotsSupport) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• Sᴜᴘᴘᴏʀᴛ •", url="https://t.me/WoFBotsSupport"),
                ],
                [
                    InlineKeyboardButton("• Rᴇᴘᴏ •", url="https://unsplash.com/photos/JBHN4EeWysE"),
                ],
            ],
        ),
    ) 

add_command_help(
    "alive",
    [
        [
            ".alive",
            "This Command for check your bot working or nt",
        ]
    ],
)
