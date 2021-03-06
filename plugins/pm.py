#-------------------------------------- https://github.com/ABotForme ------------------------------------------#
import os

from pyrogram import Client, filters
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

@Client.on_message(filters.private & filters.text)
#过滤出信息，回复/
async def pm_text(bot, message):
    if message.from_user.id == Config.ADMIN:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=Config.ADMIN,
        text=Presets.PM_TXT_ATT.format(reference_id, info.first_name,reference_id,reference_id,reference_id,reference_id, message.text),
        parse_mode="html"
    )

#@Client.on_message(filters.private & filters.media_group)
#过滤出媒体组，回复/
#async def pm_mediagroup(bot,message):
#    await bot.send_message(
#        chat_id=Config.ADMIN,
#        text=Presets.PM_MED_TES.format("1",IsShow, value)
#       # parse_mode="html"
#    )
#    if message.from_user.id == Config.ADMIN:
#        await replay_mediagroup(bot, message)
#        return
#    info = await bot.get_media_group(chat_id=message.from_user.id,message_id=message.message_id)
#    #if info == ValueError:
    #    return
#    reference_id = int(message.chat.id)
#    reference_username = message.chat.username
#    await bot.copy_media_group(
#        chat_id=Config.ADMIN,
#        from_chat_id=message.chat.id,
#        message_id=message.message_id,
#        captions=Presets.PM_MED_GRO.format(reference_id, reference_username,message.media_group_id,message.media_group_id,reference_id,reference_id),
#        parse_mode="html"
#    )

        
@Client.on_message(filters.private & filters.media)
#过滤出媒体，回复/
async def pm_media(bot, message):
    if message.from_user.id == Config.ADMIN:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=Config.ADMIN,
        text=Presets.PM_TXT_ATT.format(reference_id, info.first_name,reference_id,reference_id,reference_id,reference_id, "发送了媒体"),
        parse_mode="html"
    )
    await bot.copy_message(
        chat_id=Config.ADMIN,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=Presets.PM_MED_ATT.format(reference_id, info.first_name,reference_id,reference_id,reference_id,reference_id),
        parse_mode="html"
    )


@Client.on_message(filters.user(Config.ADMIN) & filters.text)
async def reply_text(bot, message):
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
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )

#@Client.on_message(filters.user(Config.ADMIN) & filters.media_group)
#async def replay_mediagroup(bot, message):
#    reference_id = True
#    if message.reply_to_message is not None:
#        file = message.reply_to_message
#        try:
#            reference_id = file.text.split()[2]
#        except Exception:
#            pass
#        try:
#            reference_id = file.caption.split()[2]
#        except Exception:
#            pass
#        await bot.copy_media_group(
#            chat_id=int(reference_id),
#            from_chat_id=message.chat.id,
#            message_id=message.message_id,
#            parse_mode="html"
#        )

        

@Client.on_message(filters.user(Config.ADMIN) & filters.media)
async def replay_media(bot, message):
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
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        )
