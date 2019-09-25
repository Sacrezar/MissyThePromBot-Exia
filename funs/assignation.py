import random, time
import logging
import re
from logging.handlers import RotatingFileHandler
import time

#Assignation_roles_random(people, history)
def assignation_roles_random(people, history):
    print(f"List: {people}")
    print()
    
    newRoles = []

    for role in history.keys():
        print(f"{role}: {history[role]}")
        loop = True
        while loop == True:
            roll =random.randint(0,len(people)-1)
            if people[roll] not in history[role] and people[roll] not in newRoles:
                newRoles.append(people[roll])
                loop = False
    print("------")
    print(f"New roles: {newRoles}")
    return newRoles


# dic = {
#     "Animateur": [4,1,6,10,0,5,11,7],
#     "Secrétaire": [3,9,2,4,8,11,0,5],
#     "Scribe": [5,6,10,11,2,4,1,8],
#     "Gestionnaire": [9,2,1,3,4,6,5,0]      
#     }

# def send_dic(date, roles):
#     rolling = 1
#     MyDic = {
#         "timestamp": int(time.time()),
#         "date": date,
#         "rolling": rolling,
#         "role_distrib": roles,
#     }
#     print(MyDic)

# roles = assignation_roles_random([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dic)




# send_dic("22 janvier", [0,2,4,8])