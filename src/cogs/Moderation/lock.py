import discord
from discord import Option
from discord.ext import commands
from utils.modlog import ModLog

class Lock(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Lock a channel")
    async def lock(self, ctx, channel: Option(discord.abc.GuildChannel, 'Channel to lock, default is current', required=False), reason: Option(str, 'Reason to lock the channel', required=False)):
        log = ModLog()
        await ctx.defer()
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.add_reactions = False
        overwrite.create_private_threads = False
        overwrite.create_public_threads = False
        overwrite.send_messages_in_threads = False
        if channel is None: channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond(f"Locked {channel.mention}", ephemeral=True)
        if reason is None: reason = "No reason provided"
        await log.log(ctx, "Locked channel", reason)


def setup(client):
    client.add_cog(Lock(client))