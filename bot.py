import discord
import json
import sys

"""
SETUP
"""
try:
    fp = open('config.json')
    CONFIG = json.load(fp)
    fp.close()
except:
    print("ERROR")
    print("config.json dont exist, change name sample.config.json to config.json")
    print("Dont forget to change config")
    sys.exit(0)



"""
Discord Bot
"""

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(CONFIG['token'])