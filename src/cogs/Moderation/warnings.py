import discord
from discord import Option
from discord.ext import commands
from utils.warningstore import WarningStore

class Warnings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @discord.slash_command(description="Get the warnings for a member")
    async def warnings(self, ctx, member: Option(discord.Member, 'The member to get the warnings for', required=True)):
        # Create instance of WarningStore
        warning_store = WarningStore()

        # Check if there is an entry, and if not, create one
        warning_store.create_entry(member.id)

        # Get the warnings for this member
        warnings = warning_store.get_warnings(member.id)

        # Check if the member has any warnings, if so, send them in an embed
        if len(warnings) > 0:
            # Create embed
            embed = discord.Embed(
                title=f"Warnings for {member}",
                description="".join([f"\n{index + 1}. {warning}" for index, warning in enumerate(warnings)]),
                color=discord.Color.red()
            )
        
            # Send embed
            await ctx.respond(embed=embed)
        else:
            # Send message
            await ctx.respond(f"{member.mention} has no warnings!")

def setup(client):
    client.add_cog(Warnings(client))
