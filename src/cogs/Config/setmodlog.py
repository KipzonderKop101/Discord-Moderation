import discord
from discord import Option
from discord.ext import commands
from utils.confighelper import ConfigHelper


class Setmodlog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Set the modlog channel")
    async def setmodlog(self, ctx, channel: Option(discord.abc.GuildChannel, description="The channel to set as the modlog channel", required=True)):
        config = ConfigHelper()
        config.create_modlog_entry()
        config.set_modlog_channel_id(channel.id)
        await ctx.respond(f"Set the modlog channel to {channel.name}")

def setup(client):
    client.add_cog(Setmodlog(client))