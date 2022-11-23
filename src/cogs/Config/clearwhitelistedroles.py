import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class ClearWhitelistedRoles(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Clears all whitelisted roles")
    async def clearwhitelistedroles(self, ctx):
        config = ConfigHelper()
        config.create_whitelisted_roles_entry()
        config.clear_whitelisted_roles()
        await ctx.respond("Cleared all whitelisted roles")

def setup(client):
    client.add_cog(ClearWhitelistedRoles(client))
