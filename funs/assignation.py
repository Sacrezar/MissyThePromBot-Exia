import random, time
import logging
import re
from logging.handlers import RotatingFileHandler

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Creation of the logger object that will be used to write in the logs
logger = logging.getLogger()
# Logger level at DEBUG, so he writes everything down
logger.setLevel(logging.INFO)
 
# creation of a formator  who will add time, level
# of each message when writing a message in the log
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# creation of a handler that will redirect a writing from the log to
# a file in'append' mode, with 1 backup and a maximum size of 10MB
file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 10)
# we set his level on DEBUG, we tell him he has to use the formator.
# created previously and add this handler to the logger
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
 
# creation of a second handler that will redirect each log writing to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

#available roles [GLOBAL][INFO]
role = ['leader', 'scribe', 'secretaire', 'gestionnaire']
logger.info("Roles disponibles : {}".format(role))

#File [GLOBAL][INFO]
filePath = "temp/alreadyPick.txt"

#Assignation_roles_random(people, history)
def assignation_roles_random(people, history):
    print(f"List: {people}")
    print()
    

    newRoles = {}

    for role in history.keys():
        print(f"{role}: {history[role]}")
        loop = True
        while loop == True:
            roll =random.randint(0,len(people)-1)
            if people[roll] not in history[role] and people[roll] not in newRoles:
                newRoles[role] = people[roll]
                loop = False
    print("------")
    print(f"New roles: {newRoles}")
    return newRoles


dic = {
    "Animateur": [4,1,6,10,0,5,11,7],
    "Secrétaire": [3,9,2,4,8,11,0,5],
    "Scribe": [5,6,10,11,2,4,1,8],
    "Gestionnaire": [9,2,1,3,4,6,5,0]      
    }


assignation_roles_random([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dic)