# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys
import userbot
from userbot import LOGS

from . import *
from .Session.multisession_ import Pyrogram, Telethon


from . import resources



async def memulai():
    await resources.buka(f"telethon")
    await resources.bukabot(f"assistant")

def start():
    if PandaBot:
        PandaBot.loop.run_until_complete(memulai())
        PandaBot.loop.run_until_complete(resources.join())
        LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{userbot.__version__} [TELAH DIAKTIFKAN]")



if __name__ == "__main__":
    if Database.SESSION:
        Telethon()
        start()
    if Database.PyroSESSION:
        Pyrogram()
        
    
if PandaBot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot.disconnect()
        else:
            PandaBot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
