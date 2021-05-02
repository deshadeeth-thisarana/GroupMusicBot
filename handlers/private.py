from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIOU2COfpDBwt9B2DFzXwqewtWmRvBaAAJpAAPFsQo6S-fNAfizAcIfBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by \n[Đ€Ş卄ΔĐ€€Ť卄 Ť卄ĪŞΔŘคŇΔ](https://t.me/DeshadeethThisarana).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Developer", url="https://t.me/DeshadeethThisarana")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/gangoffriends"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/gangoffriendschannel"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Mr_Group_Music_bot?startgroup=start"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/gangoffriendschannel")
                ]
            ]
        )
   )


