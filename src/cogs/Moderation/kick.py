import discord
from discord import Option
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.slash_command(description="Kick a member")
    async def kick(self, ctx, member: Option(discord.Member, 'The member to kick', required=True), reason: Option(str, 'The reason for the kick', required=False)):
        if reason == None:
            await member.kick(reason = 'No reason provided')
            await ctx.respond(f"{member} has been kicked!")
        else:
            await member.kick(reason = reason)
            await ctx.respond(f"{member.mention} has been kicked for {reason}!")

def setup(client):
    client.add_cog(Kick(client))
    