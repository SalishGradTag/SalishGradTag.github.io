from instabot import Bot

bot = Bot()

f = open("pwd.txt", "r")
pwd = f.read()

bot.login(username='salishgradtag',
          password=pwd)

text = "Eat my shorts Yash"

bot.send_message(text, 'yashjain1280')