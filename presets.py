#-------------------------------------- https://github.com/ABotForme ------------------------------------------#
class Presets(object):
    WELCOME_TEXT = """你好！ {},
我是聊天机器人！
你所发的内容我都会转发给 <a href='tg://openmessage?user_id={}'>徐坤 蔡</a>
所以你可以直接发送信息

/help 可以看到 帮助文档"""
    USER_DETAILS = "<b>PM FROM:</b>\n{}\n<b>Name:</b> {} {}\n<b>Android:</b><a href='tg://openmessage?user_id={}'>{}</a>\n<b>iOS:</b><a href='https://t.me/@id{}'>{}</a>\n<b>username: </b>@{}"
    PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n<b>Android:</b><a href='tg://openmessage?user_id={}'>{}</a>\n<b>iOS:</b><a href='https://t.me/@id{}'>{}</a>\n\n{}"
    PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Android:</b><a href='tg://openmessage?user_id={}'>{}</a>\n<b>iOS:</b><a href='https://t.me/@id{}'>{}</a>"
    PM_MED_GRO = """
<b>Message from:</b> {}
<b>Name:</b> {}
<b>Android:</b><a href='tg://openmessage?user_id={}'>{}</a>
<b>iOS:</b><a href='https://t.me/@id{}'>{}</a>
"""
    PM_MED_TES = " number {}\n {}\n {}\n"
    URL_TXT = "tg://openmessage?user_id={}"
