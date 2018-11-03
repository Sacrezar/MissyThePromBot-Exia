import discord
from discord.ext import commands

class Event:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Event(bot))