import discord
from discord import Option
from discord.ext import commands
from utils.warningstore import WarningStore

class Warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.slash_command(description="Warn a member")
    async def warn(self, ctx, member: Option(discord.Member, 'The member to mute', required=True), reason: Option(str, 'The reason for the mute', required=True)):
        # Create instance of WarningStore
        warning_store = WarningStore()

        # Check if there is an entry, and if not, create one
        warning_store.create_entry(member.id)

        # Add the warning to the list of warnings for this member
        warning_store.add_warning(member.id, reason)

        # Send message
        await ctx.respond(f"{member.mention} has been warned for {reason}!")

def setup(client):
    client.add_cog(Warn(client))
