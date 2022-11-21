import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class SetMuteRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description='Set the mute role for the server')
    async def setmuterole(self, ctx, role: Option(discord.Role, description='The role to set as the mute role', required=False)):
        config = ConfigHelper()
        config.create_mute_role_entry()
        if role is None:
            config.clear_mute_role_id()
            await ctx.respond("Cleared the mute role")
        else:
            config.set_mute_role_id(role.id)
            await ctx.respond(f"Set the mute role to {role.mention}")
            

def setup(client):
    client.add_cog(SetMuteRole(client))