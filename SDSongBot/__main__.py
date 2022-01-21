#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
Salam [{}](tg://user?id={}), Mən Mahnı Yükləmə Botuyam

 🎵
😉 Sadəcə yükləmək istədiyiniz mahnının adını mənə göndərin

.😋
      eg:```/song Taladro Kendine İyi Bak```
      
Botlarım @BTTBotlarim 🇦🇿
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="💬 Sohbet Qrupumuz", url="https://t.me/lyuksmekan"
                    ),
                    InlineKeyboardButton(
                        text="👨🏻‍💻 Sahibim", url="https://t.me/Vusaldeveloper"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ Song Aze  is online.")
idle()
