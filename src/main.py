import os
import os.path

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.getenv('TOKEN')

client = discord.Bot(intents=intents, debug_guilds=[850778582515056710])
directories = ['General', 'Moderation']

# On ready event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
