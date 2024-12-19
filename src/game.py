import random

import pandas as pd
players_path = "src/player_data.xlsx"
player_data = pd.read_excel(players_path)

game_path = "src/game_log.xlsx"
game_log = pd.read_excel(game_path)

print(player_data)

for index, row in player_data.iterrows():
    print("hhg", *row)
    '''
    ranking[row[0]] = {
        "Name" : row[4],
        "Email" : row[3],
        "HandleIG" : row[5],
        "Photo" : row[6]
    }
    '''

#print(ranking)

row = 2


