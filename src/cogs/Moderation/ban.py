import discord 
from discord import Option
from discord.ext import commands
from utils.modlog import ModLog

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.slash_command(description="Ban a member")
    async def ban(self, ctx, member: Option(discord.Member, 'The member to ban', required=True), reason: Option(str, 'The reason for the ban', required=False)):    
        log = ModLog()
        if reason is None: reason = "No reason provided"
        await member.ban(reason=reason)
        await ctx.respond(f"{member} has been banned for {reason}")
        await log.log(ctx, "Ban", reason)

def setup(client):
    client.add_cog(Ban(client))
