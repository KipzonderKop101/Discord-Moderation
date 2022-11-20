import discord
from discord import Option
from discord.ext import commands

class Unlock(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @discord.slash_command(description="Unlock a channel")
    async def unlock(self, ctx, channel: Option(discord.abc.GuildChannel, 'Channel to unlock, default is current', required=False)):
        await ctx.defer()
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.add_reactions = True
        overwrite.create_private_threads = True
        overwrite.create_public_threads = True
        overwrite.send_messages_in_threads = True
        if channel is None: channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond(f"Unlocked {channel.mention}", ephemeral=True)

def setup(client):
    client.add_cog(Unlock(client))