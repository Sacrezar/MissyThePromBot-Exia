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

#Assignation_roles_random(choix, i, nbPersonnes)
    #Choix  -> Prasit(1) ou 0
    #i      -> Numéro de groupe
    #nbPersonnes -> Nombre de personne(Len())
    #Role disponible : variable role [global] par default
def Assignation_roles_random(choix, groupNumberGlobal, nbPersonnes, tempRole=role):

    #Role disponible
    if tempRole:
        tempRole = role
    else:
        tempRole = ['leader', 'scribe', 'secretaire', 'gestionnaire']
    logger.debug(tempRole)

    #Data Recovering -> List
    myDict = {}
    with open(filePath, "r+") as f:
      for line in f:
            #Check var
            temp = re.split(',|\n|:', line)

            #Iniatialise le format des données
            for i in range(0, len(temp)):
                if(temp[i] == ''):
                    del temp[i]
                elif(temp[i] in tempRole):
                    logger.debug(temp[i])
                else:
                    temp[i] = int(temp[i])
            
            #Checks if the myDict variable needs inialization
            try:
                myDict[temp[0]]
            except:
                myDict[temp[0]] = {}

            #Adding values to the dictionnary
            myDict[temp[0]][temp[1]] = temp[2:]

            #Check values [DEBUG]
            logger.debug("Numero deja passer dans les roles suivant : {}".format(myDict))
    #Close the file
    f.closed

    #Initialize myDict if alreadyPick.txt is empty
    if(myDict == {}):
        for iGroup in range(1,3):
            myDict[iGroup] = {}
            for iRole in role:
                myDict[iGroup][iRole] = []


    #Valeur recupèrer
    logger.debug("Valeur recuperer : {}".format(myDict))

    #Random value
    randValue = getTirage(myDict[groupNumberGlobal], time.time(), nbPersonnes, tempRole,)
    logger.info("valeur random : {}".format(randValue))

    finalization(myDict, randValue, 8, groupNumberGlobal)

    return randValue

#Returns an item from the list
def getTirage(mylist, seedValue, maxUser, role):
    #Variable local
    random.seed(seedValue)
    randValue = random.randint(0, maxUser)
    randReturn = {}
    logger.debug("RandValue : {}".format(randValue))

    #Draw on all the roles
    for i in role:
        #Checks if there is a value to recover
        try:
            #If one value has already been taken, take another value
            while(randValue in mylist[i] or randValue in randReturn.values()):
                #Infinite loop in order too change randValue
                if(randValue == 0):
                    seedValue += randValue+1
                else:
                    seedValue += randValue
                #Lance un nouveau random
                random.seed(seedValue)
                randValue = random.randint(0, maxUser)
                logger.debug("{} IDTemporaire : {}".format(i, randValue))
            
        #Take a different value
        except:
            #logger.info("Mylist[{}] doesn't exist, random value : ".format(i))
            while(randValue in randReturn.values()):
                # Infinite loop in order too change randValue
                if(randValue == 0):
                    seedValue += randValue+1
                else:
                    seedValue += randValue
                #new random
                random.seed(seedValue)
                randValue = random.randint(0, maxUser)
                logger.debug("{} IDTemporaire : {}".format(i, randValue))
    
        #adding value in a dict
        randReturn[i] = randValue
        #Giving information about ID 
        logger.debug("{} ID : {}".format(i, randReturn))

    #Renvoie les valeurs recuperer
    logger.debug("Numero recuperer avant le return getTirage() : {}".format(randReturn))
    return randReturn

#Returns the names of the selected people
    #Update the function parameters
    #getName(randValue, myDict)
def getName(randValue, mylist, i):
    try:
        return mylist[i][randValue]
    except:
        return -1

#Recreate alreadyPick file
def finalization(alreadyPick, randomList, arrayRange, groupNumber):
    stemp = ""
    stempIn = ""
    #Add picked value in dictionnary 
    logger.info(alreadyPick)
    for lineRole in role:
        try:
            #Add value in the dictionnary
            alreadyPick[groupNumber][lineRole].append(randomList[lineRole])
        except:
            #Try failed, check if role in dictionnary exist
            alreadyPick[groupNumber][lineRole] = [randomList[lineRole]]

    #[1, 2, 3]      
    for keyOut in alreadyPick:
        #['leader', 'scribe', 'secretaire', 'gestionnaire']
        for keyIn in alreadyPick[keyOut]:
            #Initialise la detection de chaine
            stempIn = str(keyOut) + ":" + keyIn + ":" 

            #Delete element out of range, arrayRange var int
            if(len(alreadyPick[keyOut][keyIn]) > arrayRange):
                del alreadyPick[keyOut][keyIn][:len(alreadyPick[keyOut][keyIn])-arrayRange]
                logger.debug("The array reached max element value, NEWARRAY = {}".format(alreadyPick[keyOut][keyIn]))

            #for i in alreadyPick[keyOut][keyIn]:
            for i in range(len(alreadyPick[keyOut][keyIn])):
                stempIn += str(alreadyPick[keyOut][keyIn][i]) + ","
            
            #Initialise LOCAL var to inject in file alreadyPick.txt
            stemp += stempIn[:-1] + "\n"
            logger.debug("String send in record file = {}".format(stempIn[:-1]))
    logger.info("FILE = {}".format(stemp))

    #Modify alreadyPick.txt for next assignement
    the_file = open(filePath, 'w')
    the_file.write(stemp)
    the_file.close()

def createFile():
    the_file = open(filePath, 'w')
    the_file.close()

