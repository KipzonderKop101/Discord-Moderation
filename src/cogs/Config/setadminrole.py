import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class SetAdminRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description='Set the admin role for the server')
    async def setadminrole(self, ctx, role: Option(discord.Role, description='The role to set as the admin role', required=False)):
        config = ConfigHelper()
        config.create_admin_role_entry()
        if role is None:
            config.clear_admin_role_id()
            await ctx.respond("Cleared the admin role")
        else:
            config.set_admin_role_id(role.id)
            await ctx.respond(f"Set the admin role to {role.mention}")

def setup(client):
    client.add_cog(SetAdminRole(client))