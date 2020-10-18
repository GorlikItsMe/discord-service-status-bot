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
        
        service.status = True
        service.service = service
        service.status_title = service.name
        service.status_desc  = "{0.players.online}/{0.players.max} {1} ms".format(status_res, int(status_res.latency))
    except:
        service.status = False
        service.service = service
        service.status_title = service.name
        service.status_desc  = "Offline"


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

    service.service = service
    service.status_title = service.name
    host = service.host.split(":")[0]
    port = int(service.host.split(":")[1])
    if checkPort(host, port):
        service.status = False
        service.status_desc  = "Offline"
    else:
        service.status = True
        service.status_desc  = "Online"

def url_service(service):
    r = requests.get(service.url, headers = {'User-Agent': 'Discord Status Bot'})

    service.status_title = service.name
    if r.status_code != 200:
        service.status = False
        service.status_desc  = "HTTP {0}".format(r.status_code)
    else:
        service.status = True
        service.status_desc  = "Online"

