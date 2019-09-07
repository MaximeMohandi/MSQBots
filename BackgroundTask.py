import asyncio
import CommandFunction as cf
from discord.ext import commands
from datetime import datetime
from datetime import timedelta  
from threading import Timer

#info_du_monde = 521607979280236546
channelId=565845358261829641
x=datetime.now()
y= x + timedelta(days=1, hours=0, minutes=0, seconds=0, microseconds=0)
y= y.replace(hour=9,minute=0,second=0,microsecond=0)
secs=(y-x).total_seconds()

async def GetNewsEveryMorning(bot):
    if datetime.now().hour == 9:
        await bot.wait_until_ready()
        channel = bot.get_channel(channelId) # channel ID goes here
        while not bot.is_closed():
            await cf.DisplayAll(channel,'all')
            await asyncio.sleep(secs)
    

