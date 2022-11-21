import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper

class Unmute(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Unmute a member")
    async def unmute(self, ctx, member: Option(discord.Member, 'The member to unmute', required=True), reason: Option(str, 'The reason for the unmute', required=False)):
        # Check if member has a muted role
        config = ConfigHelper()
        if reason == None: reason = 'No reason provided'

        if not config.get_mute_role_id():
            await ctx.respond("There is no muted role set up! Please use `/setmuterole` to set one up!")
        else:
            muted_role = discord.utils.get(ctx.guild.roles, id=config.get_mute_role_id())
            if muted_role in member.roles:
                await member.remove_roles(muted_role, reason=reason)
                await ctx.respond(f"{member.mention} has been unmuted for {reason}!", ephemeral=True)
            else:
                await ctx.respond(f"{member.mention} is not muted!")

def setup(client):
    client.add_cog(Unmute(client))