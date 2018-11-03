import discord
from discord.ext import commands
from funs import date as d

class Normies:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        await self.bot.say('Pong!')

        #give the date
    @commands.command(pass_context=True)
    async def date(self, ctx):
        date = " ".join(d.getDateInList())
        await self.bot.send_message(ctx.message.channel, "```xl\n'{}'\n```".format(date))

def setup(bot):
    bot.add_cog(Normies(bot))