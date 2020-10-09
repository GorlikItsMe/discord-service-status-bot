# discord-service-status-bot
This is discord bot to display in pritty embed info about status of your service

# Setup Heroku
Link repo with heroku
create Config Var with name `CONFIG`
in this variable paste config.json
now go to section Setup for everyone


# Setup local
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
now go to section Setup for everyone


# Setup for everyone
On channel where you want have stats send
`@botname setuphere`
You will get message with channelid and messageid.
Place this values in config and restart bot

