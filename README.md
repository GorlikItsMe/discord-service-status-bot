# discord-service-status-bot
This is discord bot to display in pritty embed info about status of your service

# How to setup
```
python3 -m venv venv
.\venv\Scripts\Activate.ps1
source venv\bin\activate
python3 -m pip install --upgrade pip
pip install -r .\requirements.txt
```
Rename sample.config.json to config.json and change token. 
Then
```
python3 bot.py
```
On channel where you want have stats send
`@botname setuphere`
You will get message with channelid and messageid.
Place this values in config and restart bot

# Setup Heroku
Do everythink like before
create Config Var with name `CONFIG`
in this variable paste config.json
Start bot

# Supported check types
* minecraft - Minecraft game server
* port - Check every service what you can connect using port
* url - Check if url return 200 - you can make php script on your website what checking something and return 400 if something is wrong
