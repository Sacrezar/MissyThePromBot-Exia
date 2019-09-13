import os
import discord
import time

from discord.ext import commands
from funs import assignation, date
from database import query as q
from database import db_init as dbin
from database import rolling

class Admin:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def init(self, ctx):
        if ctx.message.author.server_permissions.administrator:
            lsdic = {
                "name": ctx.message.server.name,
                "discord" : ctx.message.server.id
            }

            lgdic = []
            for role in ctx.message.server.roles:
                gdic = {
                "name": role.name,
                "discord" : role.id
                }
                lgdic.append(gdic)

            lmdic = []
            for member in self.bot.get_all_members():
                member_role = []
                for role in member.roles:
                    member_role.append(role.id)
                mdic = {
                    "name": member.display_name,
                    "discord": member.id,
                    "groups": member_role,
                    "admin": member.server_permissions.administrator,
                }
                lmdic.append(mdic)

                # dbin.init(lsdic, lgdic, lmdic)
        else:
            channel = ctx.message.channel
            messages = []

            await self.bot.send_message(channel,"`\nYou're not allowed to\n`")

            async for message in self.bot.logs_from(channel, 2):
                messages.append(message)
            await self.bot.delete_messages(messages)   
            
    @commands.command(pass_context=True)
    async def croll(self, ctx):
        if q.is_he_admin(ctx.message.server.id,ctx.message.author.id):
            server = ctx.message.server.id
            message = ctx.message.content.split(" ")
            channel = ctx.message.channel
            to_remove = ['"', '<','>','@', '!', '&', '#']
            dates = []
            roles = []

            for x in message:
                x = [y for y in x if y not in to_remove]
                x = ''.join(x)

                y = "".join(x[:2].split())
                z = "".join(x[2:].split())

                # name
                if y == "-n":
                    name = z
                # mode
                elif y == "-m":
                    mode = z
                # roles
                elif y == "-r":
                    roles.extend(z.split(","))
                # channel
                elif y == "-c":
                    channel = z
                # participants
                elif y == "-p":
                    participants = z
                # dates
                elif y == "-d": 
                    dates.extend(z.split(","))
                else:
                    if " ".join(x.split()).lower() != "croll":
                        print("{} cant be used".format(x))
                        
            if not roles: 
                await self.bot.send_message(channel,"`No selected roles`")
            else:
                print(rolling.create_roll(name, server, mode, roles, channel, participants, dates))

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