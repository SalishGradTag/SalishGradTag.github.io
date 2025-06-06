import random
import json
import urllib.parse
import math
import os
import time

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
        return "default.png"
    return (urllib.parse.unquote(path).split("/")[-1]).replace(" ", "")

for index, row in player_data.iterrows():
    names.append(row["Name"])
    players[row["Name"]] = {
        "Name" : row["Name"],
        "Email" : row["Email"],
        "HandleIG" : row["HandleIG"],
        "Photo" : getPath(row["Photo"]),
        "Tagger" : "",
        "Date" : "",
        "Ranking" : -1,
        "Alive" : True,
        "Tags" : 0,
        "Last Tagged": 0,
        "Target": "--",
        "HTML" : "",
        "Points" : 0,
    }

num = len(names)
for index, row in game_log.iterrows():
    command = row["Command"]
    p1 = row["Para1"]
    p2 = row["Para2"]
    date = row["Date"]
    unix = row["Unix"]
    if (command=="Point"):
        players[p1]["Tags"]+=1
        players[p1]["Last Tagged"] = unix
    elif (command=="Shuffle"):
        names.sort(key=lambda x:players[x]["Alive"], reverse=True)
        a = list(range(0,num))
        print(names)
        random.Random(p1).shuffle(a)
        for i in range(0, num):
            #print(a[i])
            players[names[a[i]]]["Target"] = names[a[(i+1)%num]]
            print(names[a[i]], names[a[(i+1)%num]])
        print("\n\n\n\n\n")

    elif (command=="Tag"):
        players[p1]["Tags"]+=1
        players[p1]["Last Tagged"] =unix
        players[p1]["Date"] = str(date)[5:10]
        players[p2]["Alive"] = False
        players[p2]["Last Tagged"] =unix
        players[p2]["Date"] = str(date)[5:10]

        players[p2]["Tagger"] = p1
        players[p1]["Target"] = players[p2]["Target"]
        players[p2]["Target"] = "--"
        num-=1

    elif (command=="Negative Point"):
        players[p1]["Tags"]-=1

    elif (command=="Remove"):
        del players[p1]
        names = list(filter(lambda a: a != p1, names))

# Stable Sort
for name in names:
    if players[name]["Alive"]:
        players[name]["Last Tagged"] = time.time()
    players[name]["Points"] = (players[name]["Last Tagged"] - 1740384000) / 86400
    players[name]["Points"] += players[name]["Tags"]

names.sort(key=lambda x:players[x]["Last Tagged"],reverse=True)
names.sort(key=lambda x:players[x]["Points"],reverse=True)
names.sort(key=lambda x:players[x]["Alive"],reverse=True)


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

# HTML setting
for name in names:
    if (players[name]["Alive"]):
        players[name]["HTML"] += '<img style="width:100px;" src="../photos/' + players[name]["Photo"] + '"><br> Rank: ' + str(players[name]["Rank"]) + '<br>' + players[name]["Name"]
    else:
        players[name]["HTML"] += f'<img style="width:100px; position:absolute" src="../Images/TaggedStamp.png"><img style="width:100px;" src="../photos/{players[name]["Photo"]}"><br>Rank: {players[name]["Rank"]}<br> {players[name]["Name"]}'
        players[name]["HTML"] += f'<br>Tagged by {players[name]["Tagger"]} on {players[name]["Date"]}'
    
    if (players[name]["Tags"]>0):
        players[name]["HTML"] += f'<br>{players[name]["Tags"]} tags'
        
        
json_data = {
    "num" : num,
    "names" : names,
    "players" : players,
}

with open('src/players2.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
    