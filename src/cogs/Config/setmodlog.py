import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper


class Setmodlog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Set the modlog channel")
    async def setmodlog(self, ctx, channel: Option(discord.abc.GuildChannel, description="The channel to set as the modlog channel", required=False)):
        config = ConfigHelper()
        config.create_modlog_entry()
        if channel is None:
            config.clear_modlog_channel_id()
            await ctx.send("Cleared the modlog channel")
        else:
            config.set_modlog_channel_id(channel.id)
            await ctx.send(f"Set the modlog channel to {channel.mention}")

def setup(client):
    client.add_cog(Setmodlog(client))