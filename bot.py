#!/usr/bin/env python
# bot.py
import os
import json
import discord
#from dotenv import load_dotenv

# Import secret.json as secret[]
with open('secret.json', 'r') as myfile:
    data=myfile.read()
secret = json.loads(data)
TOKEN = secret['OAuth2Token']

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!'}

client.run(TOKEN)
