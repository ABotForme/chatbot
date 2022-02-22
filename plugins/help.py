#-------------------------------------- https://github.com/ABotForme ------------------------------------------#

import os

from pyrogram import Client, filters

from presets import Presets

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup

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

##        text="您点击了开始，请从这里发送信息以联系 XXX 吧！"
        
        text=Presets.WELCOME_TEXT.format(message.from_user.first_name,Config.ADMIN),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "设置中文", url="https://t.me/setlanguage/zhcncc"
                    ),
                    InlineKeyboardButton("秘密藏宝箱", url="https://t.me/TTreasures"),
                ],
                [InlineKeyboardButton("联系作者", url = Presets.URL_TXT.format(Config.ADMIN))],
            ]
        ),
        reply_to_message_id=message.message_id
    )

    await bot.send_message(

        chat_id=Config.ADMIN,

        text=Presets.USER_DETAILS.format(
            "点击了开始",

            info.first_name,

            info.last_name,

            info.id,info.id,info.id,info.id,

            info.username,
        )

    )


@Client.on_message(filters.private & filters.command('help'))
#帮助

async def help_me(bot, message):

 #   if message.from_user.id == Config.ADMIN:

  #      return

    info = await bot.get_users(user_ids=message.from_user.id)

    await bot.send_message(

        chat_id=message.chat.id,

        text="他还没设置帮助文档，请自己摸索！",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "三郎百宝箱", url="https://t.me/MySecretWarehouse"
                    ),
                    InlineKeyboardButton("设置中文", url="https://t.me/setlanguage/zhcncc"),
                ],
                [InlineKeyboardButton("联系作者", url = Presets.URL_TXT.format(Config.ADMIN))],
            ]
        ),
        reply_to_message_id=message.message_id
    )

    await bot.send_message(

        chat_id=Config.ADMIN,

        text=Presets.USER_DETAILS.format(
            "点击了帮助",

            info.first_name,

            info.last_name,

            info.id,info.id,info.id,info.id,

            info.username,
        )

    )
