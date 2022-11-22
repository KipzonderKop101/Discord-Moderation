import discord
from utils.confighelper import ConfigHelper

class ModLog:
    config = ConfigHelper()

    async def log(self, ctx, action, reason=None):
        # Get the mod log channel
        mod_log_channel = self.config.get_modlog_channel_id()
        if mod_log_channel is None:
            return

        # Get the mod log channel
        mod_log_channel = ctx.guild.get_channel(mod_log_channel)

        # Create the embed
        embed = discord.Embed(
            title=f"{action} | {ctx.author}",
            description=f"**User:** {ctx.author.mention}\n**Reason:** {reason}",
            color=discord.Color.green()
        )

        # Send the embed
        await mod_log_channel.send(embed=embed)