from discord.ext import commands
import discord
import datetime

def getDateInList(extradays=0):
    dayList = (
        'Lundi', #Monday
        'Mardi', #Tuesday
        'Mercredi', #Wednesday
        'Jeudi',  #Thursday
        'Vendredi', #Friday
        'Samedi', #Saturday
        'Dimanche') #Sunday

    monthList = (
        'janvier', #january
        'février', #february
        'mars', #march
        'avril', #april
        'mai', #may
        'juin', #june
        'juillet', #july
        'août', #august
        'septembre', #septembre
        'octobre', #octobre
        'novembre', #november
        'décembre') #december

    dayName = dayList[datetime.datetime.today().weekday()+extradays]
    dayInMonth = datetime.datetime.today().day
    month = monthList[datetime.datetime.today().month-1]
    year = datetime.datetime.today().year

    dateString = [str(dayName), str(dayInMonth), str(month), str(year)]
    # print(" ".join(dateString))   

    return dateString