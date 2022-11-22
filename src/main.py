import os
import os.path

import discord

from dotenv import load_dotenv
from discord.ext import commands
from utils.modlog import ModLog

load_dotenv()
log = ModLog()

intents = discord.Intents.default()
intents.message_content = True

TOKEN = os.getenv('TOKEN')

client = discord.Bot(intents=intents, debug_guilds=[850778582515056710])
directories = ['Config', 'General', 'Moderation']

# On ready event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over the server'))

@client.event
async def on_join(member):
    await log.log(member, 'Join', 'None')

@client.event
async def on_leave(member):
    await log.log(member, 'Leave', 'None')

# Reload files so that changes are applied
@client.command()
@commands.is_owner()
async def reload(ctx):
    not_loaded = []
    for directory in directories:
        for file in os.listdir(os.path.dirname(__file__) + f"/cogs/{directory}"):
            if file.endswith(".py"):
                try:
                    client.unload_extension(f"cogs.{directory}.{file[:-3]}")
                    client.load_extension(f"cogs.{directory}.{file[:-3]}")
                except Exception as e:
                    not_loaded.append(f"- **{file}** | `{e}`")
    await ctx.respond(f"Files reloaded! Errors:" + "\n".join(not_loaded))


for directory in directories:
    for file in os.listdir(os.path.dirname(__file__) + f"/cogs/{directory}"):
        if file.endswith(".py"):
            client.load_extension(f"cogs.{directory}.{file[:-3]}")
            print(f"Loaded {file}")

client.run(TOKEN)