import random
import json

import pandas as pd
players_path = "src/player_data.xlsx"
player_data = pd.read_excel(players_path)

game_path = "src/game_log.xlsx"
game_log = pd.read_excel(game_path)

#print(player_data)

def compare(p, q):
    p["Ranking"] < q["Ranking"]

rankings = []

for index, row in player_data.iterrows():
    #print("hhg", *row)
    rankings.append ({
        "Name" : row["Name"],
        "Email" : row["Email"],
        "HandleIG" : row["HandleIG"],
        "Photo" : row["Photo"],
        "Ranking" : -1,
        "Tags" : 0
        "Last Tagged": 
    })

sort(rankings, )

with open('src/rankings.json', 'w', encoding='utf-8') as f:
    json.dump(rankings, f, ensure_ascii=False, indent=4)
