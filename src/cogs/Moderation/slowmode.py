import discord
from discord import Option
from discord.ext import commands

class Slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Set slowmode in a channel")
    async def slowmode(self, ctx, channel: Option(discord.abc.GuildChannel, 'Channel to set slowmode, default is current', required=False),  amount: Option(int, "Amount of seconds to set slowmode to, default is 10", required=False)):
        if amount is None: amount = 10
        if channel is None: channel = ctx.channel
        await channel.edit(slowmode_delay=amount)
        await ctx.respond(f"Set slowmode to {amount} seconds in {channel.mention}", ephemeral=True)

def setup(client):
    client.add_cog(Slowmode(client))
