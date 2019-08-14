import discord
from discord.ext import commands
from funs import date as d

class Normies:
    def __init__(self, bot):
        self.bot = bot

    # PING PONG
    @commands.command()
    async def ping(self):
        await self.bot.say('Pong!')

    #give the date
    @commands.command(pass_context=True)
    async def date(self, ctx):
        date = d.getDate()
        await self.bot.send_message(ctx.message.channel, "```xl\n'{}'\n```".format(date))
    
    @commands.command()
    async def help(self):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name='Mais donc... Docteur Qui ?')
        embed.add_field(name="!ping", value="Pong", inline=False)
        embed.add_field(name="!date", value="Savoir la date", inline=False)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Normies(bot))
