# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Interuksi", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://drive.google.com/file/d/1TzmuSj05qF6Sm5Z_CSm3AGUCBx4Oe0F0/view?usp=sharing"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

Hey kamu selamat datang di Dimas Anime Dl, Di sini Kamu dapat Mengunduh semua Anime secara GRATIS :) ,Join channel supoort @botdimasdoang 
!!!

__Harap baca semua petunjuk tentang bot sebelum berselancar...__

Lihat /whats_new untuk mengetahui tentang pembaruan terbaru...""", reply_markup=reply_markup, parse_mode="markdown")
