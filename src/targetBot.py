#Instabot messaging bot
#Logan Singh

import random
import json
import urllib.parse
import math
import os

#from instabot import Bot

#bot = Bot()

# bot.login(username= "salishgradtag", password= "tbd")


with open('src/players.json', 'r') as json_File:
    sample_load_file=json.load(json_File)

    names = sample_load_file["names"]
    players = sample_load_file["players"]

    for name in names:
        print(players[name]["HandleIG"], players[name]["Name"])

    '''
    rows, cols, = (len(names1), 3)
    players = [['--']*cols]*rows
    print(players)
    '''