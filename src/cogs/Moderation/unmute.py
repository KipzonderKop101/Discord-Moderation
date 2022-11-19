import discord
from discord import Option
from discord.ext import commands

class Unmute(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Unmute a member")
    async def unmute(self, ctx, member: Option(discord.Member, 'The member to unmute', required=True), reason: Option(str, 'The reason for the unmute', required=False)):
        # Check if member has a muted role
        if reason == None: reason = 'No reason provided'
        if discord.utils.get(ctx.guild.roles, name="Muted") in member.roles:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(mutedRole, reason=reason)
            await ctx.respond(f"{member.mention} has been unmuted!")
        elif discord.utils.get(ctx.guild.roles, name="muted") in member.roles:
            mutedRole = discord.utils.get(ctx.guild.roles, name="muted")
            await member.remove_roles(mutedRole, reason=reason)
            await ctx.respond(f"{member.mention} has been unmuted!")
        else:
            await ctx.respond(f"{member.mention} is not muted!")


def setup(client):
    client.add_cog(Unmute(client))