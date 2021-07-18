# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Dev Info is Completely Optional

def dev_info(client, message):
    keyb = [
        [InlineKeyboardButton("Support 🌹", url="https://t.me/botdimasdoang")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    message.reply_text("""dibuat oleh Dimasrmdani.

Language: [Python3](https://www.python.org/)

Website: [DarkSkull7 Site](https://darkskull7.my.to)

Server: Linux

Silakan bagikan bot jika Anda menyukainya :)""", reply_markup=reply_markup, parse_mode="markdown")