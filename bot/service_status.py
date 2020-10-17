from mcstatus import MinecraftServer
import socket
from contextlib import closing
import requests

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
        stat.desc  = "Offline"
        return stat


def port_service(service):
    def checkPort(hostname, port, timeout=2):
        try:
            sock = socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
            sock.settimeout(timeout)
            portOpen = sock.connect((hostname, port))
            sock.close()
            return True
        except:
            return False

    stat = ServiceStatus()
    stat.service = service
    stat.title = service.name
    host = service.host.split(":")[0]
    port = int(service.host.split(":")[1])
    if checkPort(host, port):
        stat.status = False
        stat.desc  = "Offline"
    else:
        stat.status = True
        stat.desc  = "Online"
    return stat

def url_service(service):
    r = requests.get(service.url, headers = {'User-Agent': 'Discord Status Bot'})

    stat = ServiceStatus()
    stat.service = service
    stat.title = service.name
    if r.status_code != 200:
        stat.status = False
        stat.desc  = "HTTP {0}".format(r.status_code)
    else:
        stat.status = True
        stat.desc  = "Online"
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
