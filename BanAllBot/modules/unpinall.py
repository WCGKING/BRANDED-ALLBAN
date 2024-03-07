from BanAllBot import app,SUDO,BOT_ID
from pyrogram import filters

@app.on_message(filters.command("unpinall") & filters.user(SUDO))
async def unpin_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_pin_messages==True
    if bot_permission:
        try:
            await app.unpin_all_chat_messages(chat_id)
            await msg.reply_text("ᴜɴᴘɪɴɴᴇᴅ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.")
        except Exception:
            pass
    else:
        await msg.reply_text("ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs")
