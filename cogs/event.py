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
        print("Tomorrow is {}".format(date.getDateInList(1)[0]))
        while True:
            if (date.getDateInList(1)[0] == 'lundi' or date.getDateInList(1)[0] == 'Mercredi'):
                listG1 = []
                listG2 = []
                listG3 = []
                listG1A = []
                listG2A = []
                listG3A = []    
                #Groups recovery
                for member in self.bot.get_all_members(): 
                    try:
                        print("This is: " + member.display_name + " " + member.id + " " + str(member.roles[2]) + " & " + str(member.roles[1]))

                        if(str(member.roles[2]) == "G1"):
                            listG1.append(member.display_name)
                        
                        if(str(member.roles[2]) == "G2"):
                            listG2.append(member.display_name)

                        if(str(member.roles[2]) == "G3"):
                            listG3.append(member.display_name)

                        if(str(member.roles[1]) == "G1A"):
                            listG1A.append(member.display_name)
                        
                        if(str(member.roles[1]) == "G2A"):
                            listG2A.append(member.display_name)

                        if(str(member.roles[1]) == "G3A"):
                            listG3A.append(member.display_name)
                    except Exception as e:
                        print("{} : [{}]".format(member.display_name,e))

                print(listG1) 
                print(listG2)
                print(listG3)
                print("-----")
                print(listG1A) 
                print(listG2A)
                print(listG3A)
                               
                if (date.getDateInList(1)[0] == 'Mercredi'):
                    assigner = assignation.Assignation_roles_random(0, 4, len(listG1A)-1)
            #        logger.info("G1 : {}".format(assigner))
                    tirLeader1 = listG1A[assigner['leader']]
                    tirSecret1 = listG1A[assigner['secretaire']]
                    tirScrib1 = listG1A[assigner['scribe']]
                    tirTkeeper1 = listG1A[assigner['gestionnaire']]
                    
                    assigner = assignation.Assignation_roles_random(0, 5, len(listG2A)-1)
            #        logger.info("G2 : {}".format(assigner))
                    tirLeader2 = listG2A[assigner['leader']]
                    tirSecret2 = listG2A[assigner['secretaire']]
                    tirScrib2 = listG2A[assigner['scribe']]
                    tirTkeeper2 = listG2A[assigner['gestionnaire']] 

                    day = " ".join(date.getDateInList(1))

                    await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n```fix\n{0} - Anglais\n```".format(day))
                    await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629943918985237>:```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'\n```".format(tirLeader1, tirSecret1, tirScrib1, tirTkeeper1))
                    await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629942371287043>:```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'\n```".format(tirLeader2, tirSecret2, tirScrib2, tirTkeeper2))
 
        #         #Calling assignation function
                assigner = assignation.Assignation_roles_random(0, 1, len(listG1)-1)
        #        logger.info("G1 : {}".format(assigner))
                tirLeader1 = listG1[assigner['leader']]
                tirSecret1 = listG1[assigner['secretaire']]
                tirScrib1 = listG1[assigner['scribe']]
                tirTkeeper1 = listG1[assigner['gestionnaire']]
                    
                #Calling assignation function
                assigner = assignation.Assignation_roles_random(0, 2, len(listG2)-1)
        #        logger.info("G2 : {}".format(assigner))
                tirLeader2 = listG2[assigner['leader']]
                tirSecret2 = listG2[assigner['secretaire']]
                tirScrib2 = listG2[assigner['scribe']]
                tirTkeeper2 = listG2[assigner['gestionnaire']]       

                day = " ".join(date.getDateInList(1))

                await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n```fix\n{0}\n```".format(day))
                await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629943918985237>:```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'\n```".format(tirLeader1, tirSecret1, tirScrib1, tirTkeeper1))
                await self.bot.send_message(discord.Object(id='499515804589490178'),"⠀\n<@&374629942371287043>:```prolog\nAnimateur    : '{0}' \nSecretaire   : '{1}' \nScribe       : '{2}' \nGestionnaire : '{3}'\n```".format(tirLeader2, tirSecret2, tirScrib2, tirTkeeper2))
                
            await asyncio.sleep(86400)

def setup(bot):
    bot.add_cog(Event(bot))