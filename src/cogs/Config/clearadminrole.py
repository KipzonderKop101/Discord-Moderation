import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class ClearAdminRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Clears the admin role")
    async def clearadminrole(self, ctx):
        config = ConfigHelper()
        config.create_admin_role_entry()
        config.clear_admin_role_id()
        await ctx.respond("Cleared the admin role")

def setup(client):
    client.add_cog(ClearAdminRole(client))