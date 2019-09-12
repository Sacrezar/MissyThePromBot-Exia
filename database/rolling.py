from pymongo import MongoClient
# from database.connexion import co_to_DB as c
from connexion import co_to_DB as c


def create_roll(name, server, mode, roles, channel, participants, dates):
    myRoll = c()["Rolling"]

    try:
        id = myRoll.find().sort("id",-1)[0]["id"]+1
    except Exception as e: 
        print("Error : [{}]".format(e))
        id = 0

    if not myRoll.find_one({"server": server, "name" : name}):
        roll = {
            "id":id,
            "name":name,
            "server":server,
            "mode":mode,
            "roles": roles,
            "channels": channel,
            "participants": participants,
            "dates": dates
        }

        myRoll.insert_one(roll)

        return 0
    else: 
        return 1


def update_channel(name, server, channel):
    myRoll = c()["Rolling"]

    query = {"server": server, "name" : name}
    pushvalue = {"$set": {"channel": channel}}

    myRoll.update(query, pushvalue)    


def add_date(name, server, dates):
    myRoll = c()["Rolling"]

    for date in dates:
        if date in myRoll.find_one({"server": server, "name" : name})["dates"]:
            dates.remove(date)

    query = {"server": server, "name" : name}
    pushvalue = {"$push": {"dates": {"$each": dates }}}

    myRoll.update(query, pushvalue)


def remove_date(id=None, name=None, server=None, dates=None):
    myRoll = c()["Rolling"]

    if id is not None:
        query = {"id":id}
        print(id)
    else:
        query = {"server": server, "name" : name}
        print(id)
    pullvalue = {"$pull": {"dates": {"$in": dates }}}

    myRoll.update(query, pullvalue)


def add_to_history(date, rolling, role_distrib):
    myHist = c()["History"]

    history = {
        "date": date,
        "rolling": rolling,
        "role_distrib": role_distrib
    }

    myHist.insert_one(history)

    remove_date(id=rolling, dates=date)

    return 0