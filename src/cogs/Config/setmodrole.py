import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class SetModRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description='Set the mod role for the server')
    async def setmodrole(self, ctx, role: Option(discord.Role, description='The role to set as the mod role', required=False)):
        config = ConfigHelper()
        config.create_mod_role_entry()
        if role is None:
            config.clear_mod_role_id()
            await ctx.respond("Cleared the mod role")
        else:
            config.set_mod_role_id(role.id)
            await ctx.respond(f"Set the mod role to {role.mention}")

    
def setup(client):
    client.add_cog(SetModRole(client))
    