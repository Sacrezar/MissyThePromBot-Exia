from pymongo import MongoClient
# from database.connexion import co_to_DB as c
from connexion import co_to_DB as c

# how_many_servers
def how_many_servers():
    return c()["Servers"].count()

# is_he_admin
def is_he_admin(discord_id_serv, discord_id_m):
    myserv = c()["Servers"]
    mymembers = c()["Members"]
    query_to_serv = { "discord": discord_id_serv}
    query_to_members = { "discord": discord_id_m }
    server = myserv.find_one(query_to_serv)
    member = mymembers.find_one(query_to_members)

    try: 
        if server["id"] in member["adminOn"]:
            return True
        else: 
            return False
    except Exception as e: 
        print("Error : [{}]".format(e))
        return "You have to init the server" 

# roll_on_date
def roll_on_date(discord_id_serv, date):
    myroll = c()["Rolling"]
    
    query = { "dates": date}
    return myroll.find(query)

# whos_in_group
def whos_in_group(group_discord):
    mygroup = c()["Groups"]
    mymembers = c()["Members"]
    
    query_to_group = {"discord": group_discord}
    id=mygroup.find_one(query_to_group)["id"]
    query_to_members = { "groups_id": id }
    return mymembers.find(query_to_members)


data = roll_on_date(0,"Dimanche 22 Septembre 2019")
for x in data:
    if x["mode"] == "Group":
        id = x["id"]
        name = x["name"]
        participants = "<@&" + x["participants"] + ">"
        roles = x["roles"]
        channel = x["channel"]
        print(f"{id} - {channel} - {name} - {participants} - {roles}")

        datagain = whos_in_group(x["participants"])
        mydic = {}
        for y in datagain:
            idd=y["id"]
            namee = y["name"]
            print(f"{idd} : {namee}")
            mydic[y["id"]] = y["name"]
            liste = list(mydic.keys())
        print(liste)
        print(mydic.get(1))