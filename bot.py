import os
import inspect
from random import randint
import discord
from discord.ext import commands

from funs import date
from database import connexion

#login
coDic = connexion.login()

#Bot setup
bot = commands.Bot(description=coDic.get('desc'), command_prefix=coDic.get('prefix'))
bot.remove_command('help')
owner = coDic.get('owner')

exts = []
#reading file and adding them to exts if they end by ".py"
print("cogs is filled with : ", end="")
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        print(file, end=" - ")
        l = list('cogs.{}'.format(file))[0:-3]
        cfiles = "".join(l)
        exts.append(cfiles)
print()

#Online event
@bot.event
async def on_ready(): 

    print("\n")
    print("[*] I'm in, {}".format(coDic.get('join_message')))
    print('[*] Name: {}, Owner: {}'.format(bot.user.name,owner))
    print('Launched at {} on {}'.format(date.WhatHourIsIt(),date.getDate()))

    ng = coDic.get('playing')[randint(0,len(coDic.get('playing'))-1)]

    await bot.change_presence(game=discord.Game(name=ng))    

#Load & Unlod commands
@bot.command(pass_context=True)
async def load(ctx, exts):
    if(ctx.message.author.id == owner):
        try:
            bot.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))
    else:
        print('{} tried to use {}'.format(ctx.message.author, inspect.stack()[0][3]))

@bot.command(pass_context=True)
async def unload(ctx, exts):
    if(ctx.message.author.id == owner):
        try:
            bot.load_extension(extension)
            print('Unloaded {}'.format(extension))
        except Exception as e:
            print('{} cannot be unloaded. [{}]'.format(extension, e))
    else:
        print('{} tried to use {}'.format(ctx.message.author, inspect.stack()[0][3]))

#loading extension when online
if __name__ == '__main__':
    for extension in exts:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('{} cannot be loaded. [{}]'.format(extension, e))

#connect the bot
bot.run(coDic.get('token'))