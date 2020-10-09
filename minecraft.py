from mcstatus import MinecraftServer

async def server_status(CONFIG, message):
    server = MinecraftServer.lookup(CONFIG['minecraft_default'])
    status_res = server.status()
    await message.channel.send("Description: " + status_res.description + "\r\n" +
                               "Version: " + status_res.version.name + "\r\n" +
                               "Players online: " + repr(status_res.players.online) + "/" + repr(status_res.players.max) + "\r\n" +
                               "Server version: " + status_res.version.name + "\r\n")