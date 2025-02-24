import json
# from pprint import pprint

json_file = 'src/players.json'
messages = []

with open(json_file) as json_data:
    data = json.load(json_data)

    names = data["names"]
    players = data["players"]

    for name in names:
        if (name=="Harnagad Sidhu"):
            cur = {}
            cur["email"] = players[name]["Email"]
            cur["message"] = f"""
Sorry Harangad still testing <br>

Hi <at>{cur["email"]}</at>, <br>
Your target is {players[name]["Target"]}. <br>

Please read the <a href="https://salishgradtag.ca/2025/rules">rules</a> <br>

If you have questions or want to submit a tag, message myself, Logan Singh or @salishgradtag on instagram.
"""
        
            messages.append(cur)
        
with open('src/messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4)