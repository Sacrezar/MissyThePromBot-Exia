from pymongo import MongoClient
from database.connexion import co_to_DB as c
# from connexion import co_to_DB as c


def is_he_admin(discord_id_serv, discord_id_m):
    myserv = c()["Servers"]
    mymember = c()["Members"]
    query_to_serv = { "discord": discord_id_serv}
    query_to_members = { "discord": discord_id_m }
    server = myserv.find_one(query_to_serv)
    member = mymember.find_one(query_to_members)

    try: 
        if server["id"] in member["adminOn"]:
            return True
        else: 
            return False
    except Exception as e: 
        print("Error : [{}]".format(e))
        return "You have to init the server" 



