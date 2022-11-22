import discord
from discord import Option
from discord.ext import commands
from utils.modlog import ModLog

class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Purge messages in a channel")
    async def purge(self, ctx, channel: Option(discord.abc.GuildChannel, 'Channel to purge, default is current', required=False),  amount: Option(int, "Amount of messages to purge, default is 10", required=False), reason: Option(str, 'Reason for purging this channel', required=False)):
        if amount is None: amount = 10
        if channel is None: channel = ctx.channel
        if reason is None: reason = "No reason provided"

        log = ModLog()

        await channel.purge(limit=amount)
        await ctx.respond(f"Purged {amount} messages in {channel.mention}", ephemeral=True)

        await log.log(ctx, "Purged messages", reason)

def setup(client):
    client.add_cog(Purge(client))
