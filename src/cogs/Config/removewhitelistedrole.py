import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class RemoveWhiteListedRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description='Remove a role from the whitelist')
    async def removewhitelistedrole(self, ctx, role: Option(discord.Role, description='The role to remove from the whitelist', required=True)):
        config = ConfigHelper()
        config.create_whitelisted_roles_entry()
        whitelisted_roles = config.get_whitelisted_roles()
        if role.id not in whitelisted_roles:
            await ctx.send('That role is not whitelisted!')
        else:
            whitelisted_roles.remove(role.id)
            config.set_whitelisted_roles(whitelisted_roles)
            await ctx.respond(f'Removed {role.mention} from the whitelist!')

def setup(client):
    client.add_cog(RemoveWhiteListedRole(client))