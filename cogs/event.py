import discord
import asyncio
from discord.ext import commands
from funs import assignation, date
from database import query as q
from database import rolling as r


class Event():
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.bg_task = self.bot.loop.create_task(self.autoroll())
        self.bg_task = self.bot.loop.create_task(self.groups_update())

    async def autoroll(self):
        await self.bot.wait_until_ready()
        print("Tomorrow is {}".format(date.getDate(1)))
        while True:
            for x in range(q.how_many_servers()):
                #retrieve data
                data = q.roll_on_date(x,"Dimanche 22 Septembre 2019")

                for roll in data:
                    if roll["mode"] == "Group":
                        
                        #declarations
                        member_dic = {}
                        id = roll["id"]
                        participants = "<@&" + roll["participants"] + ">"
                        roles = roll["roles"]
                        channel = roll["channel"] 
                        members = q.whos_in_group(roll["participants"])

                        for member in members:
                            member_dic[member["id"]] = member["name"]

                        id_list = list(member_dic.keys()) 
                        print("roles are: ",roles)

                    history = q.get_history(id, roles, len(id_list))
                    chosen_ones = assignation.assignation_roles_random(id_list, history)
                    # prepare to send message
                    embed = discord.Embed(colour=discord.Colour.dark_gold())
                    embed.set_author(name = date.getDate(1))
                    for role in range(len(roles)):
                        embed.add_field(name = roles[role], value = member_dic.get(chosen_ones[role]), inline=False)
                    # send message
                    await self.bot.send_message(destination=discord.Object(id=channel),content = participants, embed=embed)
                    embed.clear_fields()
                    r.add_to_history("Dimanche 22 Septembre 2019", id, chosen_ones)

            await asyncio.sleep(86400)
    
    async def groups_update(self):
        await self.bot.wait_until_ready()
        while True:
            await asyncio.sleep(10)

def setup(bot):
    bot.add_cog(Event(bot))