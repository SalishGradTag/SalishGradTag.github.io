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
Hi <at>{cur["email"]}</at>, <br>
Targets are shuffling!

Your new target is {players[name]["Target"]}. <br>
You may not tag any previous targets you have had. <br><br>

Good Luck!
"""
            messages.append(cur)
        
with open('src/messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4)