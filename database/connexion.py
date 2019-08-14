from pymongo import MongoClient
from random import randint

def co_to_DB():
    client = MongoClient(port=27017)
    return client["ExiaThePromBot"]

def login(): 
    mycol = co_to_DB()["Config"]

    return(mycol.find_one())

