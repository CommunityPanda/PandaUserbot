# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys
import userbot
from userbot import LOGS

from . import *
from .Session.multisession_ import *
from pytgcalls import idle as pytgcalls


from . import resources


"""
async def memulai():
    await resources.buka(f"telethon")
    await resources.bukabot(f"assistant")
"""

def start():
    if PandaBot:
        PandaBot.loop.run_until_complete(resources.memulai())
        PandaBot.loop.run_until_complete(resources.join())
        LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{userbot.__version__} [TELAH DIAKTIFKAN]")
    if PandaBot:
        PandaBot.send_message(PRIVATE, THON_ON.format(PandaBot.me.username, version.__version__, cmdhr))
    if PandaBot2:
        PandaBot2.me = PandaBot2.get_me()
        PandaBot2.send_message(PRIVATE, THON_ON.format(PandaBot2.me.username, version.__version__, cmdhr))
    if PandaBot3:
        PandaBot3.me = PandaBot3.get_me()
        PandaBot3.send_message(PRIVATE, THON_ON.format(PandaBot3.me.username, version.__version__, cmdhr))
             


if __name__ == "__main__":
    if Database.SESSION:
        Telethon()
        resources.ClientMultiTelethon()
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

if PandaBot2:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot2.disconnect()
        else:
            PandaBot2.run_until_disconnected()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if PandaBot3:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PandaBot3.disconnect()
        else:
            PandaBot3.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if vcbot and call_py:
    try:
        if len(sys.argv) not in (1, 3, 4):
            vcbot.disconnect()
        else:
            vcbot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
        pytgcalls()
