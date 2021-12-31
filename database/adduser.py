from pyrogram import Client
from database.access import tellybots
from pyrogram.types import Message
from config import Config

async def AddUser(bot: Client, cmd: Message):
    if not await tellybots.is_user_exist(cmd.from_user.id):
        await tellybots.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{(await bot.get_me()).username} !!"
            )


