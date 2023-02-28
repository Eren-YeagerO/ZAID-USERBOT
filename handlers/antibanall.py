from pyrogram import Client, filters
import time

from main import bot1 as app

# Define the time window in seconds
time_window = 60

# Define the maximum number of bans allowed in the time window
max_bans = 2

# Define a dictionary to keep track of the number of bans by each admin
bans_by_admin = {}

# Define a function to check if an admin has banned too many members in the time window
async def check_bans(update, user_id):
    # Get the current time
    now = time.time()

    # Remove any bans from the dictionary that are outside the time window
    bans_by_admin[user_id] = [ban for ban in bans_by_admin[user_id] if now - ban < time_window]

    # Count the number of bans in the time window
    num_bans = len(bans_by_admin[user_id])

    # If the admin has banned too many members in the time window, demote them
    if num_bans > max_bans:
        await app.promote_chat_member(update.chat.id, user_id, can_change_info=False, can_delete_messages=False,
                                      can_invite_users=True, can_pin_messages=False, can_promote_members=False,
                                      can_restrict_members=True)
        del bans_by_admin[user_id]
        await app.send_message(update.chat.id, f"Admin {user_id} has been demoted for banning too many members in a short period of time")

# Define a function to handle the ban event
@app.on_message(filters.private & filters.new_chat_members)
async def handle_new_chat_members(update, members):
    for member in members:
        # If an admin has banned a member, increment the ban count for that admin
        if member.is_member_banned:
            user_id = member.banned_by.id
            if user_id not in bans_by_admin:
                bans_by_admin[user_id] = []
            bans_by_admin[user_id].append(time.time())
            await check_bans(update, user_id)
