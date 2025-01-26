import random
import json
import urllib.parse
import math
import os

import pandas as pd

players_path = "src/player_data.xlsx"
player_data = pd.read_excel(players_path)

game_path = "src/game_log.xlsx"
game_log = pd.read_excel(game_path)

#print(player_data)

players = {}
names = []

def getPath(path):
    if (type(path)==float and math.isnan(path)):
        return ""
    return (urllib.parse.unquote(path).split("/")[-1]).replace(" ", "")

for index, row in player_data.iterrows():
    names.append(row["Name"])
    players[row["Name"]] = {
        "Name" : row["Name"],
        "Email" : row["Email"],
        "HandleIG" : row["HandleIG"],
        "Photo" : getPath(row["Photo"]),
        "Ranking" : -1,
        "Alive" : True,
        "Tags" : 0,
        "Last Tagged": 0 
    }

for index, row in game_log.iterrows():
    if (row["Command"]=="Tag"):
        players[row["Person 1"]]["Tags"]+=1
        players[row["Person 1"]]["Last Tagged"] = row["Unix"]
        players[row["Person 2"]]["Alive"] = False
        players[row["Person 2"]]["Last Tagged"] = row["Unix"]

# Stable Sort
names.sort(key=lambda x:players[x]["Last Tagged"], reverse=True)
names.sort(key=lambda x:players[x]["Tags"], reverse=True)
names.sort(key=lambda x:players[x]["Alive"], reverse=True)

rank = 0

for i in range(len(names)):
    cur = names[i] 
    rank+=1
    if (i>0):
        prev = names[i-1]
        if (players[cur]["Alive"] == players[prev]["Alive"] and
            players[cur]["Tags"] == players[prev]["Tags"] and
            players[cur]["Last Tagged"] == players[prev]["Last Tagged"]):
            rank-=1
    players[cur]["Rank"] = rank

json_data = {
    "names" : names,
    "players" : players
}

with open('src/players.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
