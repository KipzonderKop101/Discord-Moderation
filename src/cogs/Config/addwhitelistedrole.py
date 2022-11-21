import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class AddWhiteListedRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description='Add a role to the whitelist')
    async def addwhitelistedrole(self, ctx, role: Option(discord.Role, description='The role to add to the whitelist', required=True)):
        config = ConfigHelper()
        config.create_whitelisted_roles_entry()
        whitelisted_roles = config.get_whitelisted_roles()
        if role.id in whitelisted_roles:
            await ctx.send('That role is already whitelisted!')
        else:
            whitelisted_roles.append(role.id)
            config.set_whitelisted_roles(whitelisted_roles)
            await ctx.respond(f'Added {role.mention} to the whitelist!')
        

def setup(client):
    client.add_cog(AddWhiteListedRole(client))