import discord
import json
import sys
import os
import asyncio
from datetime import datetime
import time

from bot.config import CONFIG
from bot import service_status
from bot.utils import global_status_color, last_check_time_str, update_presence
"""
Discord Bot
"""
client = discord.Client()

async def status_task():
    # CONFIG['channel_id'] == 0 OR CONFIG['status_message_id'] == 0:
    try:
        statusmsg = await client.get_channel(CONFIG.channel_id).fetch_message(CONFIG.status_message_id)
    except Exception:
        print("ERROR CONFIG channel_id and status_message_id, cant fetch status message")
        print("check permissions and if that message exist")
        return
    statusmsg = await client.get_channel(CONFIG.channel_id).fetch_message(CONFIG.status_message_id)
    await statusmsg.edit(content="Loading status...")
    
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Starting..."))  

    while True:
        check_time_start = time.time()

        for s in CONFIG.services:
            if s.type == "minecraft":
                service_status.minecraft(s)
            elif s.type == "port":
                service_status.port_service(s)
            elif s.type == "url":
                service_status.url_service(s)
            else:
                print("Unsupported type:", s.type)

        check_time_ms = int((time.time() - check_time_start)*1000)

        # update Embed
        embed = discord.Embed(colour=global_status_color(CONFIG.services), description="", timestamp=datetime.utcnow())
        embed.set_author(name=CONFIG.embed_title)
        embed.set_footer(text=last_check_time_str(check_time_ms))
        for s in CONFIG.services:
            embed.add_field(name=s.title_full(), value=s.status_desc, inline=False)
        await statusmsg.edit(content="", embed=embed)

        # update activity
        await update_presence(client, CONFIG.services)

        await asyncio.sleep(CONFIG.update_time_sek)

    
@client.event
async def on_ready():
    print("Invite link: https://discord.com/api/oauth2/authorize?client_id={0}&permissions=280640&scope=bot".format(client.user.id))
    print('Name: {0.user}'.format(client))
    client.loop.create_task(status_task())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    
    tag = "<@!"+str(client.user.id)+">"
    tag2 = "<@"+str(client.user.id)+">"
    if message.content.startswith(tag) or message.content.startswith(tag2):
        # removing mention
        message.content = message.content.replace(tag, "")
        message.content = message.content.replace(tag2, "")
        message.content = message.content.strip()

        if message.content.startswith('setuphere'):
            thismsg = await message.channel.send("Load...")
            await thismsg.edit(content="If you want status display here add this to config end reload\n```\"channel_id\": {0}, \n\"status_message_id\": {1}, ```".format(message.channel.id, thismsg.id))

        else:
          await message.channel.send("usage @mention setuphere")  

try:
    client.run(CONFIG.token)
except:
    print("Invalid token :(")
    sys.exit(0)