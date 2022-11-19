import discord 
from discord import Option
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.slash_command(description="Ban a member")
    async def ban(self, ctx, member: Option(discord.Member, 'The member to ban', required=True), reason: Option(str, 'The reason for the ban', required=False)):    
        if reason == None:
            await member.ban(reason = 'No reason provided')
            await ctx.respond(f"{member} has been banned!")
        else:
            await member.ban(reason = reason)
            await ctx.respond(f"{member.mention} has been banned for {reason}!")

def setup(client):
    client.add_cog(Ban(client))
