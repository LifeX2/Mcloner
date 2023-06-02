import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *

os.system("apt install git curl python3-pip ffmpeg -y")


API_ID = ""163
API_HASH = ""
TOKEN = ""

ZAID = Client("Pyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


@ZAID.on_message(filters.private & filters.command("start"))
async def hello(client: ZAID, message: Message):
    await message.reply("**Hey! It's Just a Cloner Bot example source Code**")


@ZAID.on_message(filters.private & filters.command("clone"))
async def gnsStr(bot: ZAID, msg: Message):
    """Command format will be /clone <repo> <clone as> <ccloned Directry> <start command>"""
    chat = msg.chat
    zaid = await msg.reply("Usage:\n\n /clone <GitHub url> <clone as (name)> <start command>.\n\n ex: /clone https://github.com/ITZ-ZAID/Cloner Zaid python3 main.py")
    cmd = msg.command
    repo = msg.command[1]
    extract = msg.command[2]
    bash = msg.command[4]
    try:
        await zaid.edit("Cloning Your Codes")
        os.system(f"git clone {repo} {extract} && cd {extract} && pip3 install -U -r requirements.txt && python3 {bash}") 
        await zaid.edit("Done ✅")  
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

ZAID.start()
idle()
