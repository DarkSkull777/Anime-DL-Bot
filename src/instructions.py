# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    query.answer("Mohon Baca Dengan Teliti!!!")
    keyb = [
        [InlineKeyboardButton("Cari Anime Online", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""**Bot ini bisa Mendapatkan Anime favorit Anda dan Ini menyediakan Tautan Unduhan GRATIS dengan server tercepat (Google drive).**

**Hal-hal yang Perlu Diperhatikan :-**

__👉Karena gogoanime sering mengubah domainnya, Bot akan sering melakukan pemeliharaan. Jangan khawatir, bot akan tetap online selama maintenance.__

__👉Untuk streaming di ponsel, buka tautan dengan VLC Media Player. Anda juga dapat menggunakan MX Player.__

__👉Untuk streaming di PC, gunakan aliran jaringan pemutar media VLC.__

__👉Untuk unduhan, cukup buka tautan di browser.__

**Itu saja, Anda semua terjebak, mulai saja dan nikmati anime favorit Anda :D**

**Ketik /search Untuk mencari anime...**""", parse_mode="markdown", reply_markup=reply_markup)
