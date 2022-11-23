import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class ClearMuteRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Clears the mute role")
    async def clearmuterole(self, ctx):
        config = ConfigHelper()
        config.create_mute_role_entry()
        config.clear_mute_role_id()
        await ctx.respond("Cleared the mute role")

def setup(client):
    client.add_cog(ClearMuteRole(client))
    