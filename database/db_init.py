from pymongo import MongoClient
from database.connexion import co_to_DB as c
# from connexion import co_to_DB as c

def update():
    print('yolo')

def init(sdic, gdic, mdic):

    # TODO - Verif if data is already registered.

    g = c()["Groups"]
    s = c()["Servers"]
    m = c()["Members"]

    # groups
    try:
        id_g = g.find().sort("id",-1)[0]["id"]+1
    except Exception as e: 
        print("Error : [{}]".format(e))
        id_g = 0

    groups_list = []
    for groups in gdic:
        group = {
            "id":id_g,
            "name": groups["name"],
            "discord": groups["discord"]
        }
        g.insert_one(group)
        groups_list.append(id_g)
        id_g += 1 

    # server
    try:
        id_s = s.find().sort("id",-1)[0]["id"]+1
    except Exception as e: 
        print("Error : [{}]".format(e))
        id_s = 0

    # members
    try:
        id_m = m.find().sort("id",-1)[0]["id"]
    except Exception as e: 
        print("Error : [{}]".format(e))
        id_m = 0

    id_s = 0
    id_m = 0

    
    members_list = []
    for members in mdic:
        glist = []
        redondance = False
        try:
            redondance = m.find_one({"discord": members["discord"]})
        except:
            redondance = False

        if not redondance:
            for gr in members["groups"]:
                result = g.find_one({"discord" : gr})
                glist.append(result["id"])
            
            if members["admin"] == True:
                adminOn = id_s
            else:
                adminOn = None

            member = {
                "id": id_m,
                "name": members["name"],
                "discord": members["discord"],
                "groups_id": glist,
                "servers_id": [id_s],
                "adminOn": [adminOn]
            }
            m.insert_one(member)
            members_list.append(id_m)
            id_m += 1
        else: 
            members_list.append(redondance["id"])

    server = {
        "id":id_s,
        "name": sdic["name"],
        "discord": sdic["discord"],
        "members_id" : members_list,
        "groups_id": groups_list,
        "authorized_chan": []
    }
    s.insert_one(server)
