import json
# from print import print

json_file = 'src/players.json'
messages = []

with open(json_file) as json_data:
    data = json.load(json_data)

    names = data["names"]
    players = data["players"]

    for name in names:
        if (players[name]["Alive"]):
            cur = {}
            cur["email"] = players[name]["Email"]
            cur["message"] = f"""
Hello <at>{cur["email"]}</at>, <br>
Targets are off! You may tag anyone still in the game if they are not immune. <br><br>
Good Luck!
"""
            messages.append(cur)
        
with open('src/messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4)