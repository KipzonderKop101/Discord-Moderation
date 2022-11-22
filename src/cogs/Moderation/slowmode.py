import discord
from discord import Option
from discord.ext import commands
from utils.modlog import ModLog

class Slowmode(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Set slowmode in a channel")
    async def slowmode(self, ctx, channel: Option(discord.abc.GuildChannel, 'Channel to set slowmode, default is current', required=False),  amount: Option(int, "Amount of seconds to set slowmode to, default is 10", required=False), reason: Option(str, 'Reason to set slowmode', required=False)):
        if amount is None: amount = 10
        if channel is None: channel = ctx.channel
        if reason is None: reason = "No reason provided"

        log = ModLog()

        await channel.edit(slowmode_delay=amount)
        await ctx.respond(f"Set slowmode to {amount} seconds in {channel.mention}", ephemeral=True)
        await log.log(ctx, "Set slowmode", reason)

def setup(client):
    client.add_cog(Slowmode(client))
