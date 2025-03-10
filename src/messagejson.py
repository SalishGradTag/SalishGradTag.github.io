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
Nice job surviving so far! <br><br>

Your new target is {players[name]["Target"]}. <br>
You may not tag any pervious targets you have had. <br><br>

Here are the <a href="https://salishgradtag.ca/2025/rules">rules</a>.
There have been some minor changes to account for special cases.

If you have questions or want to submit a tag, message myself, Logan Singh, or @salishgradtag on instagram.
<br><br>
Thanks for playing and good luck!
"""
            messages.append(cur)
        
with open('src/messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4)