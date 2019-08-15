import os
import discord
import time

from discord.ext import commands
from funs import assignation, date
from database import query as q

class Admin:
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(pass_context=True)
    # async def dtroll(self, ctx):
    #     # Ajout de date sous format dd/mm/aaaa ou D mm aaaa ou D M

    # async def roll(self, ctx):

    #Clear function
    @commands.command(pass_context = True)
    async def clear(self, ctx, amount=99):
        channel = ctx.message.channel
        messages = []

        if q.is_he_admin(ctx.message.server.id,ctx.message.author.id):
            async for message in self.bot.logs_from(channel, limit=int(amount+1)):
                messages.append(message)
            numberOfMessages = len(messages)-1
            await self.bot.delete_messages(messages)
            
            await self.bot.send_message(channel,'` {} messages deleted`'.format(numberOfMessages))
        
            async for message in self.bot.logs_from(channel, 1):
                messages.append(message)
            await self.bot.delete_messages(messages)

        else:
            await self.bot.send_message(channel,"`\nYou're not allowed to\n`")

            async for message in self.bot.logs_from(channel, 2):
                messages.append(message)
            await self.bot.delete_messages(messages)


def setup(bot):
    bot.add_cog(Admin(bot))