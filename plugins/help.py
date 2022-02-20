#-------------------------------------- https://github.com/Pradeepnagal ------------------------------------------#

import os

from pyrogram import Client, filters

from presets import Presets

if bool(os.environ.get("ENV", False)):

    from sample_config import Config

else:

    from config import Config

@Client.on_message(filters.private & filters.command('start'))
#开始

async def start_me(bot, message):

 #   if message.from_user.id == Config.ADMIN:

  #      return

    info = await bot.get_users(user_ids=message.from_user.id)

    await bot.send_message(

        chat_id=message.chat.id,

        text="您点击了开始，请从这里发送信息以联系 @vodkaHeb 吧！"

    )

    await bot.send_message(

        chat_id=Config.ADMIN,

        text=Presets.USER_DETAILS.format(
            "开始",

            info.first_name,

            info.last_name,

            info.id, info.username,

            info.is_scam,

            info.is_restricted,

            info.status,

            info.dc_id

        )

    )
    await bot.send_message(

        chat_id=Config.ADMIN,

        text="点击了开始"

    )

@Client.on_message(filters.private & filters.command('help'))
#帮助

async def help_me(bot, message):

 #   if message.from_user.id == Config.ADMIN:

  #      return

    info = await bot.get_users(user_ids=message.from_user.id)

    await bot.send_message(

        chat_id=message.chat.id,

        text="他还没设置帮助文档，请自己摸索！"

    )

    await bot.send_message(

        chat_id=Config.ADMIN,

        text=Presets.USER_DETAILS.format(
            "帮助",

            info.first_name,

            info.last_name,

            info.id, info.username,

            info.is_scam,

            info.is_restricted,

            info.status,

            info.dc_id

        )

    )
    await bot.send_message(

        chat_id=Config.ADMIN,

        text="点击了帮助"

    )
