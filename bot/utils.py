import discord


def global_status_color(stat_array):   
    all_online = True
    for s in stat_array:
        if s.status == False:
            all_online = False
    
    all_offline = True
    for s in stat_array:
        if s.status == True:
            all_offline = False
    
    if all_online: #online
        return discord.Colour(0x2ffc00)
    elif all_offline: #ofline
        return discord.Colour(0xfc0000)
    else: #partial
        return discord.Colour(0xf8e71c)

def last_check_time_str(check_time_ms):
    if(check_time_ms < 5000):
        return "Last check took: {0} ms".format(check_time_ms)
    return "Last check took: {0} sek".format(int(check_time_ms/1000))