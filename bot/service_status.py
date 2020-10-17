from mcstatus import MinecraftServer


def minecraft(service):

    def clear_text(text):
        for x in "0123456789abcdefklmnor":
            text = text.replace("§"+x, "")
        return text

    server = MinecraftServer.lookup(service.host)
    try:
        status_res = server.status()
        stat = ServiceStatus()
        stat.status = True
        stat.service = service
        stat.title = service.name
        stat.desc  = "{0.players.online}/{0.players.max} {1} ms".format(status_res, int(status_res.latency))
        return stat
    except:
        stat = ServiceStatus()
        stat.status = False
        stat.service = service
        stat.title = service.name
        stat.desc  = "Offline".format()
        return stat


class ServiceStatus():
    status = False
    service = None # Service form config
    title = ""
    desc = ""

    def status_emoji(self):
        if self.status:
            return ":white_check_mark:"
        return ":x:"
    
    def title_full(self):
        return self.status_emoji()+" "+self.title
