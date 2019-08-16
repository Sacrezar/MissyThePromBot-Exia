from pymongo import MongoClient
from database.connexion import co_to_DB as c
# from connexion import co_to_DB as c


def is_he_admin(discord_id_serv, discord_id_m):
    mycol = c()["Servers"]

    myquery = { "discord_id_serv": discord_id_serv}

    data = mycol.find(myquery)
    mydic = data[0]["details"]["membres"]

    for x in mydic:
        if x["discord_id_m"] == discord_id_m:
            if x["isHeAdmin"] == 1:
                return True

    return False

def new_assigned_group(discord_id_serv, discord_id_m, discord_id_g):
    mycol = c()["Servers"]

    myquery = { "discord_id_serv": discord_id_serv}

    data = mycol.find(myquery)    
    mydic = data[0]["details"]["groups"]
    
    for x in mydic:
        if x["discord_id_g"] == discord_id_g:
            id = x["id_g"]







