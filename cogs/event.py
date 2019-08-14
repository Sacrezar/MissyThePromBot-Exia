import discord
import asyncio
from discord.ext import commands
from funs import assignation, date


class Event():
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.autoroll())

    #Group Rotation (Tuesday & Wednesday)
    async def autoroll(self):
        await self.bot.wait_until_ready()
        print("Tomorrow is {}".format(date.getDate(1)))
        while True:
            # if date+1 == one date in toRoll["dates"] and toRoll["flag"] == 1
            await asyncio.sleep(86400)

def setup(bot):
    bot.add_cog(Event(bot))