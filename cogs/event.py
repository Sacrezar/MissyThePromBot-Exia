import discord
import asyncio
from discord.ext import commands
from funs import assignation, date
from database import query as q

class Event():
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.autoroll())
        self.bg_task = self.bot.loop.create_task(self.groups_update())

    #Group Rotation (Tuesday & Wednesday)
    async def autoroll(self):
        await self.bot.wait_until_ready()
        print("Tomorrow is {}".format(date.getDate(1)))
        while True:
            # if date+1 == one date in toRoll["dates"] and toRoll["flag"] == 1
            await asyncio.sleep(86400)
    
    async def groups_update(self):
        await self.bot.wait_until_ready()
        while True:
            id_serv = 1
            id_m = 1
            list_id_g = 1
            q.new_assigned_group(id_serv, id_m, list_id_g)
            await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(Event(bot))