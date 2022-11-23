import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class ClearModLog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Clears the mod log channel")
    async def clearmodlog(self, ctx):
        config = ConfigHelper()
        config.create_modlog_entry()
        config.clear_modlog_channel_id()
        await ctx.respond("Cleared the mod log channel")

def setup(client):
    client.add_cog(ClearModLog(client))