from discord.ext import commands
import discord
from datetime import datetime
from calendar import monthrange

# accept day, month and year values as number
def getDate(flag=0,day=None, month=None, year=None):
    
    Mydict = {
        'Monday'   :  'Lundi',
        'Tuesday'  :  'Mardi',
        'Wednesday':  'Mercredi',
        'Thursday' :  'Jeudi',
        'Friday'   :  'Vendredi',
        'Saturday' :  'Samedi',
        'Sunday'   :  'Dimanche',
        'January'  :  'Janvier',
        'February' :  'Février',
        'March'    :  'Mars',
        'April'    :  'Avril',
        'May'      :  'Mai',
        'June'     :  'Juin',
        'July'     :  'Juillet',
        'August'   :  'Août',
        'September':  'Septembre',
        'October'  :  'Octobre',
        'November' :  'Novembre', 
        'December' :  'Décembre' 
    }
    now = datetime.now()

    if not day:
        day = now.day+flag
    if not month:
        month = now.month
    if not year: 
        year = now.year

    # prevent from errors due to the flag
    _ , x = monthrange(year,month)
    while day>x:
        day-=x
        month+=1
        if month>12:
            month-=12
            year+=1
        _ , x = monthrange(year,month)

    day, daynum, month, year = datetime(year, month, day).strftime("%A %d %B %Y").split(" ")

    # convert to french
    day = Mydict.get(day)
    month = Mydict.get(month)

    dateString = " ".join([day, str(daynum), month, str(year)])

    return dateString

def WhatHourIsIt():
    return datetime.now().time()
