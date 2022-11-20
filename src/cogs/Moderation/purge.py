import discord
from discord import Option
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Purge messages in a channel")
    async def purge(self, ctx, channel: Option(discord.abc.GuildChannel, 'Channel to purge, default is current', required=False),  amount: Option(int, "Amount of messages to purge, default is 10", required=False)):
        if amount is None: amount = 10
        if channel is None: channel = ctx.channel

        await channel.purge(limit=amount)
        await ctx.respond(f"Purged {amount} messages in {channel.mention}", ephemeral=True)

def setup(client):
    client.add_cog(Purge(client))
