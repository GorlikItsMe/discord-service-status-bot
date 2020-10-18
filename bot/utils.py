import discord
import asyncio
import time


def global_status_color_int(services):   
    all_online = True
    for s in services:
        if s.status == False:
            all_online = False
    
    all_offline = True
    for s in services:
        if s.status == True:
            all_offline = False

    if all_online: #online
        return 0
    elif all_offline: #ofline
        return 1
    else: #partial
        return 2

def global_status_color(services):   
    n = global_status_color_int(services)
    
    if n==0: #online
        return discord.Colour(0x2ffc00)
    elif n==1: #ofline
        return discord.Colour(0xfc0000)
    else: #partial
        return discord.Colour(0xf8e71c)

def last_check_time_str(check_time_ms):
    if(check_time_ms < 5000):
        return "Last check took: {0} ms".format(check_time_ms)
    return "Last check took: {0} sek".format(int(check_time_ms/1000))

async def update_presence(client, services):
    out = ""
    for s in services:
        if s.status:
            out = out +"✅"
        else:
            out = out +"❌"
    
    n = global_status_color_int(services)
    if n==0: #online
        await client.change_presence(status=discord.Status.online, activity=discord.Game(out))  
    elif n==1: #ofline
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(out))  
    else: #partial
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(out))  
        
    print(time.time(), out)

