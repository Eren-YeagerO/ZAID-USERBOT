from main import bot1

@bot1.on_message(filters.command("banall"))
async def _(bot1, msg):
    print("getting memebers from {}".format(msg.chat.id))
    async for i in bot1.get_chat_members(msg.chat.id):
        try:
            await bot1.ban_chat_member(chat_id =msg.chat.id,user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id,msg.chat.id))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            print(e)
        except Exception as e:
            print(" failed to kicked {} from {}".format(i.user.id,e))           
    print("process completed")
