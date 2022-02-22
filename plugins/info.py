#-------------------------------------- https://github.com/Pradeepnagal ------------------------------------------#
import os

from pyrogram import Client, filters
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.user(Config.ADMIN) & filters.command(['info']))
#回复消息
async def user_info(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
    info = await bot.get_users(reference_id)
    await message.delete()
    await bot.send_message(
        chat_id=Config.ADMIN,
        text=Presets.USER_DETAILS.format(
            "信息info",
            info.first_name,
            info.last_name,
            info.id,info.id,info.id,info.id,
            info.username,
            info.is_scam,
            info.is_restricted,
            info.status,
            info.dc_id
        )
    )
