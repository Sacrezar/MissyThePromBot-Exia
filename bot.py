import os
import inspect

from funs import date
import json
import discord
from discord.ext import commands

from Reverse import reverseClient

#Opening env file 
with open('.env.json') as f:
    env = json.load(f)
with open(env.get('config')) as e:
    config = json.load(e)

#Bot setup
bot = commands.Bot(description=config.get('desc'), command_prefix=config.get('prefix'))
reverseClient = reverseClient()
bot.remove_command('help')
owner = config.get('owners')


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
    print("[*] I'm in, {}".format(config.get('join_message')))
    print('[*] Name: {}, Owner: {}'.format(bot.user.name,owner))
    print('Launched at {} on {}'.format(date.WhatHourIsIt()," ".join(date.getDateInList())))

    #Register every new servers and members
    await reverseClient.registerServers(bot.servers)
    #await reverseClient.registerMember(bot.get_all_members);
    await bot.change_presence(game=discord.Game(name=config.get('playing')))    

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
bot.run(config.get('token'))