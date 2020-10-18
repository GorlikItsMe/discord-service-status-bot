import json
import sys
import os
import time
from .utils import seconds2str


class Config():
    token = ""
    channel_id = ""
    status_message_id = ""
    services = []
    update_time_sek = 10
    embed_title = "status"

    def __init__(self, json_config):
        self.token = json_config['token']
        self.channel_id = int(json_config['channel_id'])
        self.status_message_id = int(json_config['status_message_id'])
        self.update_time_sek = int(json_config['update_time_sek'])
        self.embed_title = json_config['embed_title']
        for s in json_config['services']:
            self.services.append(Service(s))

class Service():
    name = ""
    type = ""
    host = ""
    url = ""

    last_online = int(time.time())
    last_offline = int(time.time())
    status = False
    status_title = ""
    status_desc = ""

    def __init__(self, json_service_config):
        self.name = json_service_config["name"]
        self.type = json_service_config["type"]
        try:
            self.host = json_service_config["host"]
        except:
            pass
        try:
            self.url = json_service_config["url"]
        except:
            pass
    
    def status_emoji(self):
        if self.status:
            return ":white_check_mark:"
        return ":x:"
    
    def title_full(self):
        return self.status_emoji()+" "+self.status_title
    
    def desc_full(self):
        return self.status_desc+"\n"+self.uptime()
    
    def set_online(self):
        self.status = True
        self.last_online = int(time.time())
    
    def set_offline(self):
        self.status = False
        self.last_offline = int(time.time())
    
    def uptime(self):
        if self.last_offline > self.last_online:
            delta = self.last_offline - self.last_online
            return "Last online: "+seconds2str(delta)+" ago"

        if self.last_offline < self.last_online:
            delta = self.last_online - self.last_offline
            return "Uptime: "+seconds2str(delta)




config_str = os.environ.get('CONFIG', None)

if config_str == None:
    try:
        fp = open('config.json')
        config_json = json.load(fp)
        fp.close()
    except:
        print("ERROR")
        print("config.json dont exist, change name sample.config.json to config.json")
        print("If you use heroku you dont set CONFIG value")
        print("use sample.config.json to configure")
        sys.exit(0)

else:
    config_json = json.loads(config_str)

CONFIG = Config(config_json)