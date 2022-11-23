import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class ClearModRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Clears the mod role")
    async def clearmodrole(self, ctx):
        config = ConfigHelper()
        config.create_mod_role_entry()
        config.clear_mod_role_id()
        await ctx.respond("Cleared the mod role")

def setup(client):
    client.add_cog(ClearModRole(client))