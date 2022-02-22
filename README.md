# 🤖 聊天机器人 🤖
一个简单的机器人，可用作管理个人消息的个人助理。

### 💠 帮助
在繁忙的日程中，我们不能一直接收来自不需要或者是不必要的用户个人信息。这个机器人是该问题的解决方案。所有的个人信息都可以通过这个机器人进行管理，我们的个人聊天将会是安全和干净的。

### 在 HeroKu 上部署:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ABotForme/chatBot)

### 💠 使用方法

- 用户可以通过信息或者媒体消息向机器人发送消息
- 机器人会将消息作为 PM 发送给管理员用户ID
- 管理员需要回复机器人中收到的 消息（文本和媒体）
- 回复的消息将在机器人中作为 PM 发送给用户
- 命令 ```/info``` 作为对收到的任何聊天的回复将提供有关 PM 用户的基本信息(仅限管理员)


### 💠 机器人命令 

```
# User Commmands
/start or /help- Start Message

# Admin Commmands
/info - Basic Information about the user

#vars
TG_BOT_TOKEN - Your Bot Token
APP_ID - Your APP ID
API_HASH - Your API Hash
ADMIN - Admin User Id.

```
### 💠 Credits
[Pradeep Nagal](https://t.me/fojipk) for his [Pyrogram](https://github.com/pyrogram/pyrogram) Library

[Vodka Heb](https://t.me/VodkaHeb) for his [chatbot](https://github.com/ABotForme/chatbot) Library
